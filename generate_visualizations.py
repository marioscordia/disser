#!/usr/bin/env python3
"""Generate all 8 bibliometric visualizations in VOSviewer/CiteSpace academic style."""

import csv
import re
import os
from collections import defaultdict, Counter
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import matplotlib.patches as mpatches
import networkx as nx
from scipy.stats import gaussian_kde

OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'visualizations')
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Paper subdirectories
BASE = os.path.dirname(os.path.abspath(__file__))
PAPER_DIRS = {
    'prisma': os.path.join(BASE, 'paper', 'Prisma'),
    'citespace': os.path.join(BASE, 'paper', 'Citespace'),
    'vosviewer': os.path.join(BASE, 'paper', 'VOSViewer'),
}
for d in PAPER_DIRS.values():
    os.makedirs(d, exist_ok=True)

# ── Load Data ──────────────────────────────────────────────────────────────

def load_papers():
    papers = []
    with open('sourcelist.csv', 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            papers.append(row)
    return papers

def load_references():
    refs = {}
    with open('references.txt', 'r', encoding='utf-8') as f:
        content = f.read()
    entries = re.split(r'\n\n+', content.strip())
    for entry in entries:
        entry = entry.strip()
        if not entry:
            continue
        doi_match = re.search(r'doi\.org/([^\s"]+)', entry)
        if doi_match:
            doi = 'doi.org/' + doi_match.group(1).rstrip('.')
            ref_text = re.sub(r'^\d+\s*', '', entry).strip()
            refs[doi] = ref_text
    return refs

papers = load_papers()
refs = load_references()
print(f"Loaded {len(papers)} papers and {len(refs)} references")

# ── Keyword extraction ─────────────────────────────────────────────────────

CURATED_KEYWORDS = [
    'violence detection', 'anomaly detection', 'weapon detection', 'firearm detection',
    'deep learning', 'CNN', 'LSTM', 'YOLO', 'convolutional neural network',
    'video surveillance', 'object detection', 'optical flow', 'attention mechanism',
    'transfer learning', 'real-time detection', 'pose estimation', 'GRU', 'autoencoder',
    'spatiotemporal features', 'behavior recognition', 'action recognition',
    'edge computing', 'IoT', 'CCTV', 'crowd analysis', 'skeleton-based', 'ResNet',
    'MobileNet', '3D CNN', 'feature extraction'
]

CLUSTER_RED = ['CNN', 'LSTM', 'GRU', 'ResNet', 'MobileNet', '3D CNN', 'YOLO', 'autoencoder']
CLUSTER_GREEN = ['optical flow', 'spatiotemporal features', 'action recognition', 'behavior recognition', 'skeleton-based']
CLUSTER_BLUE = ['violence detection', 'anomaly detection', 'weapon detection', 'firearm detection', 'video surveillance', 'CCTV', 'real-time detection', 'IoT', 'edge computing', 'crowd analysis']
CLUSTER_YELLOW = ['deep learning', 'attention mechanism', 'transfer learning', 'pose estimation', 'feature extraction', 'convolutional neural network', 'object detection']

def get_cluster(kw):
    if kw in CLUSTER_RED: return 'red'
    if kw in CLUSTER_GREEN: return 'green'
    if kw in CLUSTER_BLUE: return 'blue'
    if kw in CLUSTER_YELLOW: return 'yellow'
    return 'gray'

# VOSviewer-like color palette — softer, academic colors
CLUSTER_COLORS = {
    'red':    '#e15759',   # soft red
    'green':  '#59a14f',   # soft green
    'blue':   '#4e79a7',   # soft blue
    'yellow': '#f28e2b',   # soft orange/yellow
    'gray':   '#bab0ac'    # soft gray
}

CLUSTER_NAMES = {
    'red': 'Deep Learning Architectures',
    'green': 'Temporal & Motion Analysis',
    'blue': 'Application & Deployment',
    'yellow': 'Methods & Techniques'
}

def extract_keywords(papers):
    keyword_counts = Counter()
    keyword_paper_years = defaultdict(list)
    for idx, p in enumerate(papers):
        title = (p.get('Title', '') or '').lower()
        abstract = (p.get('Short description', '') or '').lower()
        text = title + ' ' + abstract
        year = int(p.get('Year', 2024) or 2024)
        for kw in CURATED_KEYWORDS:
            if kw.lower() in text:
                keyword_counts[kw] += 1
                keyword_paper_years[kw].append(year)
    return keyword_counts, keyword_paper_years

keyword_counts, keyword_paper_years = extract_keywords(papers)
print(f"Found {len([k for k,v in keyword_counts.items() if v > 0])} keywords with occurrences")

# ── Co-occurrence ───────────────────────────────────────────────────────────

def build_cooccurrence(papers):
    cooc = defaultdict(lambda: defaultdict(int))
    for p in papers:
        title = (p.get('Title', '') or '').lower()
        abstract = (p.get('Short description', '') or '').lower()
        text = title + ' ' + abstract
        found = [kw for kw in CURATED_KEYWORDS if kw.lower() in text]
        for i in range(len(found)):
            for j in range(i+1, len(found)):
                cooc[found[i]][found[j]] += 1
                cooc[found[j]][found[i]] += 1
    return cooc

cooc = build_cooccurrence(papers)

# ── Common layout params ────────────────────────────────────────────────────

def get_network_layout():
    G = nx.Graph()
    for kw, count in keyword_counts.items():
        if count > 0:
            G.add_node(kw, count=count, cluster=get_cluster(kw))
    for kw1 in keyword_counts:
        for kw2 in keyword_counts:
            if kw1 < kw2 and cooc.get(kw1, {}).get(kw2, 0) >= 2:
                G.add_edge(kw1, kw2, weight=cooc[kw1][kw2])
    pos = nx.spring_layout(G, k=3.5, iterations=100, seed=42)
    return G, pos

G, pos = get_network_layout()

def node_size_scale(count):
    return 400 + (count / max(keyword_counts.values())) * 3200

# ═════════════════════════════════════════════════════════════════════════════
# VISUALIZATION 1: vosviewer_keyword_network.png (Figure 3)
# ═════════════════════════════════════════════════════════════════════════════

def viz1_keyword_network():
    fig, ax = plt.subplots(figsize=(18, 14), dpi=200)
    ax.set_facecolor('#ffffff')
    fig.patch.set_facecolor('#ffffff')

    # Draw edges — thin, light grey, VOSviewer style
    for u, v, data in G.edges(data=True):
        w = data.get('weight', 1)
        x1, y1 = pos[u]
        x2, y2 = pos[v]
        ax.plot([x1, x2], [y1, y2], color='#c8c8c8', linewidth=w*0.35, alpha=0.55, zorder=1)

    # Draw nodes — filled circles with thin dark border
    for node in G.nodes():
        x, y = pos[node]
        count = keyword_counts[node]
        size = node_size_scale(count)
        cluster = get_cluster(node)
        color = CLUSTER_COLORS[cluster]
        ax.scatter(x, y, s=size, c=color, edgecolors='#333333', linewidth=0.8,
                   zorder=3, alpha=0.88)

    # Labels — VOSviewer places them near nodes in small font
    for node in G.nodes():
        x, y = pos[node]
        ax.annotate(node, (x, y), textcoords="offset points", xytext=(0, -15),
                    ha='center', fontsize=7.5, fontweight='normal', color='#222222',
                    zorder=4)

    # Legend — VOSviewer style, positioned top-right inside axes
    legend_patches = [mpatches.Patch(color=CLUSTER_COLORS[c], label=CLUSTER_NAMES[c])
                      for c in ['red', 'green', 'blue', 'yellow']]
    legend = ax.legend(handles=legend_patches, loc='upper right', fontsize=10,
                       framealpha=0.92, edgecolor='#cccccc', facecolor='white',
                       title='Clusters', title_fontsize=11)
    legend.get_frame().set_linewidth(0.8)

    ax.set_title('Keyword Co-occurrence Network', fontsize=20, fontweight='bold',
                 color='#222222', pad=20)
    ax.axis('off')
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    fig.tight_layout()

    fig.savefig(os.path.join(OUTPUT_DIR, 'vosviewer_keyword_network.png'),
                dpi=200, bbox_inches='tight', facecolor='white', edgecolor='none')
    fig.savefig(os.path.join(PAPER_DIRS['vosviewer'], 'vosviewer_keyword_network.png'),
                dpi=200, bbox_inches='tight', facecolor='white', edgecolor='none')
    plt.close(fig)
    print("  -> vosviewer_keyword_network.png")

viz1_keyword_network()

# ═════════════════════════════════════════════════════════════════════════════
# VISUALIZATION 2: vosviewer_overlay.png (Figure 5)
# ═════════════════════════════════════════════════════════════════════════════

def viz2_overlay():
    fig, ax = plt.subplots(figsize=(18, 14), dpi=200)
    ax.set_facecolor('#ffffff')
    fig.patch.set_facecolor('#ffffff')

    avg_years = {}
    for kw in keyword_counts:
        years = keyword_paper_years.get(kw, [])
        avg_years[kw] = np.mean(years) if years else 2024

    year_min, year_max = 2022, 2026

    # Edges
    for u, v, data in G.edges(data=True):
        w = data.get('weight', 1)
        x1, y1 = pos[u]; x2, y2 = pos[v]
        ax.plot([x1, x2], [y1, y2], color='#d0d0d0', linewidth=w*0.3, alpha=0.5, zorder=1)

    # VOSviewer temporal colormap: blue (old) → green → yellow (new)
    from matplotlib.colors import LinearSegmentedColormap
    vos_colors = ['#2c5aa0', '#4ea0c1', '#5cb860', '#b8d939', '#f5e53b']
    vos_cmap = LinearSegmentedColormap.from_list('vosviewer_temporal', vos_colors)

    norm = plt.Normalize(year_min, year_max)

    for node in G.nodes():
        x, y = pos[node]
        count = keyword_counts[node]
        size = node_size_scale(count)
        avg_y = avg_years.get(node, 2024)
        color = vos_cmap(norm(avg_y))
        ax.scatter(x, y, s=size, c=[color], edgecolors='#333333', linewidth=0.8,
                   zorder=3, alpha=0.88)
        ax.annotate(node, (x, y), textcoords="offset points", xytext=(0, -15),
                    ha='center', fontsize=7.5, fontweight='normal', color='#222222',
                    zorder=4)

    # Colorbar
    sm = plt.cm.ScalarMappable(cmap=vos_cmap, norm=norm)
    sm.set_array([])
    cbar = fig.colorbar(sm, ax=ax, shrink=0.45, aspect=35, pad=0.02)
    cbar.set_label('Average Publication Year', fontsize=13, color='#333333')
    cbar.ax.tick_params(labelsize=10, colors='#333333')
    cbar.outline.set_edgecolor('#cccccc')

    ax.set_title('Temporal Overlay — Average Publication Year per Keyword',
                 fontsize=20, fontweight='bold', color='#222222', pad=20)
    ax.axis('off')
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    fig.tight_layout()

    fig.savefig(os.path.join(OUTPUT_DIR, 'vosviewer_overlay.png'),
                dpi=200, bbox_inches='tight', facecolor='white', edgecolor='none')
    fig.savefig(os.path.join(PAPER_DIRS['vosviewer'], 'vosviewer_overlay.png'),
                dpi=200, bbox_inches='tight', facecolor='white', edgecolor='none')
    plt.close(fig)
    print("  -> vosviewer_overlay.png")

viz2_overlay()

# ═════════════════════════════════════════════════════════════════════════════
# VISUALIZATION 3: vosviewer_density.png (Figure 4)
#   VOSviewer renders density on a dark canvas with warm colormap.
#   We match that convention: dark background, yellow→orange→red heatmap.
# ═════════════════════════════════════════════════════════════════════════════

def viz3_density():
    fig, ax = plt.subplots(figsize=(18, 14), dpi=200)
    dark_bg = '#0d0d0d'
    ax.set_facecolor(dark_bg)
    fig.patch.set_facecolor(dark_bg)

    points = np.array([pos[n] for n in G.nodes()])
    if len(points) >= 4:
        weights = np.array([keyword_counts[n] for n in G.nodes()])
        kde = gaussian_kde(points.T, weights=weights / weights.sum())
        xi, yi = np.mgrid[-2.0:2.0:250j, -2.0:2.0:250j]
        zi = kde(np.vstack([xi.flatten(), yi.flatten()]))
        zi = zi.reshape(xi.shape)
        # VOSviewer density: yellow→orange→red→dark on dark background
        ax.imshow(zi, extent=[-2.0, 2.0, -2.0, 2.0], origin='lower',
                  cmap='YlOrRd', alpha=0.70, aspect='auto', zorder=1,
                  interpolation='bilinear')

    # Small white node markers (VOSviewer shows point locations)
    for node in G.nodes():
        x, y = pos[node]
        count = keyword_counts[node]
        size = 20 + (count / max(keyword_counts.values())) * 140
        ax.scatter(x, y, s=size, c='white', edgecolors='none',
                   zorder=3, alpha=0.75)

    # Label top 15 keywords in white
    top15 = sorted(keyword_counts.items(), key=lambda x: x[1], reverse=True)[:15]
    top15_names = {k for k, _ in top15}
    for node in G.nodes():
        if node in top15_names:
            x, y = pos[node]
            ax.annotate(node, (x, y), textcoords="offset points", xytext=(0, -16),
                        ha='center', fontsize=8, fontweight='bold', color='white',
                        zorder=4)

    ax.set_title('Keyword Density Map', fontsize=20, fontweight='bold',
                 color='white', pad=20)
    ax.axis('off')
    ax.set_xlim(-2.0, 2.0)
    ax.set_ylim(-2.0, 2.0)
    fig.tight_layout()

    fig.savefig(os.path.join(OUTPUT_DIR, 'vosviewer_density.png'),
                dpi=200, bbox_inches='tight', facecolor=dark_bg, edgecolor='none')
    fig.savefig(os.path.join(PAPER_DIRS['vosviewer'], 'vosviewer_density.png'),
                dpi=200, bbox_inches='tight', facecolor=dark_bg, edgecolor='none')
    plt.close(fig)
    print("  -> vosviewer_density.png")

viz3_density()

# ═════════════════════════════════════════════════════════════════════════════
# VISUALIZATION 4: citespace_burst_timeline.png (Figure 6)
#   CiteSpace style: white background, keyword labels on left,
#   year columns, grey baseline, red burst segments.
# ═════════════════════════════════════════════════════════════════════════════

def viz4_burst_timeline():
    fig, ax = plt.subplots(figsize=(14, 9), dpi=200)
    ax.set_facecolor('#ffffff')
    fig.patch.set_facecolor('#ffffff')

    top15 = sorted(keyword_counts.items(), key=lambda x: x[1], reverse=True)[:15]
    top15_kws = [k for k, _ in top15]
    years_range = list(range(2022, 2027))

    kw_year_counts = defaultdict(lambda: defaultdict(int))
    for idx, p in enumerate(papers):
        title = (p.get('Title', '') or '').lower()
        abstract = (p.get('Short description', '') or '').lower()
        text = title + ' ' + abstract
        year = int(p.get('Year', 2024) or 2024)
        for kw in top15_kws:
            if kw.lower() in text:
                kw_year_counts[kw][year] += 1

    n_kw = len(top15_kws)
    for i, kw in enumerate(reversed(top15_kws)):
        y_pos = i
        counts = {y: kw_year_counts[kw].get(y, 0) for y in years_range}

        # Grey baseline for every year with data
        for y in years_range:
            if y in kw_year_counts[kw]:
                ax.plot([y - 0.25, y + 0.25], [y_pos, y_pos],
                        color='#aaaaaa', linewidth=4, solid_capstyle='round', zorder=2)

        # Red burst: the year(s) with highest count
        max_count = max(counts.values()) if counts else 0
        if max_count > 0:
            burst_years = [y for y in years_range if counts[y] == max_count]
            for by in burst_years:
                ax.plot([by - 0.25, by + 0.25], [y_pos, y_pos],
                        color='#d73027', linewidth=7, solid_capstyle='round', zorder=3)

    # Y-axis: keyword labels
    ax.set_yticks(range(n_kw))
    ax.set_yticklabels(reversed(top15_kws), fontsize=10.5, color='#222222')
    ax.set_xticks(years_range)
    ax.set_xticklabels(years_range, fontsize=10.5, color='#222222')
    ax.set_xlim(2021.3, 2027.0)
    ax.set_ylim(-0.6, n_kw - 0.4)

    # Frequency column on the right
    for i, kw in enumerate(reversed(top15_kws)):
        count = keyword_counts[kw]
        ax.annotate(str(count), (2026.52, i), color='#d73027', fontsize=10,
                    ha='left', va='center', fontweight='bold')

    ax.annotate('Freq.', (2026.52, n_kw - 0.15), color='#555555', fontsize=9,
                ha='left', va='bottom')

    ax.set_title('Top 15 Keywords with Citation Bursts (2022–2026)',
                 fontsize=17, fontweight='bold', color='#222222', pad=18)
    ax.tick_params(colors='#333333', length=0)
    # Light gridlines for year separation
    for y in years_range:
        ax.axvline(x=y, color='#eeeeee', linewidth=0.8, zorder=0)
    for spine in ax.spines.values():
        spine.set_color('#cccccc')
    ax.yaxis.set_ticks_position('none')
    fig.tight_layout()

    fig.savefig(os.path.join(OUTPUT_DIR, 'citespace_burst_timeline.png'),
                dpi=200, bbox_inches='tight', facecolor='white', edgecolor='none')
    fig.savefig(os.path.join(PAPER_DIRS['citespace'], 'citespace_burst_timeline.png'),
                dpi=200, bbox_inches='tight', facecolor='white', edgecolor='none')
    plt.close(fig)
    print("  -> citespace_burst_timeline.png")

viz4_burst_timeline()

# ═════════════════════════════════════════════════════════════════════════════
# VISUALIZATION 5: citespace_coauthorship.png (optional, not in paper)
# ═════════════════════════════════════════════════════════════════════════════

def viz5_coauthorship():
    fig, ax = plt.subplots(figsize=(18, 14), dpi=200)
    ax.set_facecolor('#ffffff')
    fig.patch.set_facecolor('#ffffff')

    author_papers = defaultdict(list)
    author_paper_set = defaultdict(set)

    for idx, p in enumerate(papers):
        authors_str = (p.get('Authors', '') or '').strip()
        if not authors_str:
            continue
        authors = [a.strip() for a in authors_str.split(';') if a.strip()]
        formatted = []
        for a in authors:
            parts = a.split()
            if len(parts) >= 2:
                surname = parts[-1]
                initials = ''.join(p[0] for p in parts[:-1])
                formatted.append(f"{surname} {initials}.")
            else:
                formatted.append(a)
        for fa in formatted:
            author_papers[fa].append(idx)
            author_paper_set[fa].add(idx)

    G_auth = nx.Graph()
    for author, paper_set in author_paper_set.items():
        if len(paper_set) >= 1:
            G_auth.add_node(author, count=len(paper_set))

    for idx, p in enumerate(papers):
        authors_str = (p.get('Authors', '') or '').strip()
        if not authors_str:
            continue
        authors = [a.strip() for a in authors_str.split(';') if a.strip()]
        formatted = []
        for a in authors:
            parts = a.split()
            if len(parts) >= 2:
                surname = parts[-1]
                initials = ''.join(p[0] for p in parts[:-1])
                formatted.append(f"{surname} {initials}.")
            else:
                formatted.append(a)
        for i in range(len(formatted)):
            for j in range(i+1, len(formatted)):
                if formatted[i] in G_auth and formatted[j] in G_auth:
                    if G_auth.has_edge(formatted[i], formatted[j]):
                        G_auth[formatted[i]][formatted[j]]['weight'] += 1
                    else:
                        G_auth.add_edge(formatted[i], formatted[j], weight=1)

    isolated = [n for n in G_auth.nodes() if G_auth.degree(n) == 0]
    G_auth.remove_nodes_from(isolated)

    if len(G_auth) > 0:
        communities = nx.community.greedy_modularity_communities(G_auth, weight='weight')
        node_colors = {}
        palette = [CLUSTER_COLORS[c] for c in ['red', 'green', 'blue', 'yellow']]
        palette += ['#9b59b6', '#1abc9c', '#e67e22', '#e91e63']
        for ci, comm in enumerate(communities):
            for node in comm:
                node_colors[node] = palette[ci % len(palette)]

        pos_auth = nx.spring_layout(G_auth, k=2.5, iterations=100, seed=42)

        max_count = max(nx.get_node_attributes(G_auth, 'count').values())
        for node in G_auth.nodes():
            x, y = pos_auth[node]
            count = G_auth.nodes[node]['count']
            size = 120 + (count / max_count) * 1000
            color = node_colors.get(node, '#888888')
            ax.scatter(x, y, s=size, c=color, edgecolors='#333333',
                       linewidth=0.6, zorder=3, alpha=0.88)

        for u, v, data in G_auth.edges(data=True):
            x1, y1 = pos_auth[u]; x2, y2 = pos_auth[v]
            w = data.get('weight', 1)
            ax.plot([x1, x2], [y1, y2], color='#cccccc', linewidth=w*0.25,
                    alpha=0.5, zorder=1)

        for node in G_auth.nodes():
            if G_auth.nodes[node]['count'] >= 2:
                x, y = pos_auth[node]
                ax.annotate(node, (x, y), textcoords="offset points", xytext=(0, -10),
                            ha='center', fontsize=6.5, color='#333333')

    ax.set_title('Co-Authorship Network', fontsize=20, fontweight='bold',
                 color='#222222', pad=20)
    ax.axis('off')
    fig.tight_layout()

    fig.savefig(os.path.join(OUTPUT_DIR, 'citespace_coauthorship.png'),
                dpi=200, bbox_inches='tight', facecolor='white', edgecolor='none')
    fig.savefig(os.path.join(PAPER_DIRS['citespace'], 'citespace_coauthorship.png'),
                dpi=200, bbox_inches='tight', facecolor='white', edgecolor='none')
    plt.close(fig)
    print("  -> citespace_coauthorship.png")

viz5_coauthorship()

# ═════════════════════════════════════════════════════════════════════════════
# VISUALIZATION 6: citespace_trend.png (Figure 2)
#   Academic bar chart: white background, clean styling.
# ═════════════════════════════════════════════════════════════════════════════

def viz6_trend():
    fig, ax = plt.subplots(figsize=(12, 7.5), dpi=200)
    ax.set_facecolor('#ffffff')
    fig.patch.set_facecolor('#ffffff')

    years = list(range(2022, 2027))
    scopus_counts = defaultdict(int)
    wos_counts = defaultdict(int)
    for p in papers:
        year = int(p.get('Year', 2024) or 2024)
        db = (p.get('Database', '') or '').strip().lower()
        if 'scopus' in db:
            scopus_counts[year] += 1
        elif 'web of science' in db or 'wos' in db:
            wos_counts[year] += 1

    x = np.arange(len(years))
    width = 0.33

    scopus_vals = [scopus_counts[y] for y in years]
    wos_vals = [wos_counts[y] for y in years]

    # Academic colors: muted blue and red
    bars1 = ax.bar(x - width/2, scopus_vals, width, label='Scopus',
                   color='#4e79a7', edgecolor='white', linewidth=0.6)
    bars2 = ax.bar(x + width/2, wos_vals, width, label='Web of Science',
                   color='#e15759', edgecolor='white', linewidth=0.6)

    # Total count annotations
    for i, (s, w) in enumerate(zip(scopus_vals, wos_vals)):
        total = s + w
        if total > 0:
            ax.annotate(str(total), (x[i], max(s, w) + 0.6), ha='center',
                        color='#333333', fontsize=12, fontweight='bold')

    ax.set_xticks(x)
    ax.set_xticklabels(years, fontsize=13, color='#333333')
    ax.set_ylabel('Number of Publications', fontsize=13, color='#333333')
    ax.set_title('Publication Trend by Year and Database (2022–2026)',
                 fontsize=17, fontweight='bold', color='#222222', pad=18)
    ax.legend(fontsize=12, facecolor='white', edgecolor='#cccccc',
              framealpha=0.9)
    ax.tick_params(colors='#333333', labelsize=11)
    for spine in ax.spines.values():
        spine.set_color('#cccccc')
    ax.set_ylim(0, max([s+w for s, w in zip(scopus_vals, wos_vals)]) * 1.2)
    # Light horizontal gridlines
    ax.yaxis.grid(True, color='#eeeeee', linewidth=0.6)
    ax.set_axisbelow(True)
    fig.tight_layout()

    fig.savefig(os.path.join(OUTPUT_DIR, 'citespace_trend.png'),
                dpi=200, bbox_inches='tight', facecolor='white', edgecolor='none')
    fig.savefig(os.path.join(PAPER_DIRS['citespace'], 'citespace_trend.png'),
                dpi=200, bbox_inches='tight', facecolor='white', edgecolor='none')
    plt.close(fig)
    print("  -> citespace_trend.png")

viz6_trend()

# ═════════════════════════════════════════════════════════════════════════════
# VISUALIZATION 7: citespace_keyword_freq.png (optional, not in paper)
# ═════════════════════════════════════════════════════════════════════════════

def viz7_keyword_freq():
    fig, ax = plt.subplots(figsize=(14, 10), dpi=200)
    ax.set_facecolor('#ffffff')
    fig.patch.set_facecolor('#ffffff')

    top20 = sorted(keyword_counts.items(), key=lambda x: x[1], reverse=True)[:20]
    labels = [k for k, _ in reversed(top20)]
    values = [v for _, v in reversed(top20)]
    colors = [CLUSTER_COLORS[get_cluster(k)] for k, _ in reversed(top20)]

    bars = ax.barh(labels, values, color=colors, edgecolor='white', linewidth=0.6, height=0.75)
    for bar, val in zip(bars, values):
        ax.text(bar.get_width() + 0.3, bar.get_y() + bar.get_height()/2,
                str(val), va='center', color='#333333', fontsize=11, fontweight='bold')

    ax.set_xlabel('Frequency', fontsize=13, color='#333333')
    ax.set_title('Top 20 Keywords by Frequency', fontsize=17, fontweight='bold',
                 color='#222222', pad=18)
    ax.tick_params(colors='#333333', labelsize=10.5)
    for spine in ax.spines.values():
        spine.set_color('#cccccc')
    ax.set_xlim(0, max(values) * 1.15)
    ax.xaxis.grid(True, color='#eeeeee', linewidth=0.5)
    ax.set_axisbelow(True)

    legend_patches = [mpatches.Patch(color=CLUSTER_COLORS[c], label=CLUSTER_NAMES[c])
                      for c in ['red', 'green', 'blue', 'yellow']]
    ax.legend(handles=legend_patches, loc='lower right', fontsize=10,
              facecolor='white', edgecolor='#cccccc', framealpha=0.9)

    fig.tight_layout()

    fig.savefig(os.path.join(OUTPUT_DIR, 'citespace_keyword_freq.png'),
                dpi=200, bbox_inches='tight', facecolor='white', edgecolor='none')
    fig.savefig(os.path.join(PAPER_DIRS['citespace'], 'citespace_keyword_freq.png'),
                dpi=200, bbox_inches='tight', facecolor='white', edgecolor='none')
    plt.close(fig)
    print("  -> citespace_keyword_freq.png")

viz7_keyword_freq()

# ═════════════════════════════════════════════════════════════════════════════
# VISUALIZATION 8: PRISMA 2020 Flow Diagram (Figure 1)
#   Standard PRISMA 2020 template: vertical flow with side branches.
# ═════════════════════════════════════════════════════════════════════════════

def viz8_prisma():
    fig, ax = plt.subplots(figsize=(16, 18), dpi=200)
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 22)
    ax.axis('off')
    ax.set_facecolor('white')
    fig.patch.set_facecolor('white')

    # PRISMA 2020 color scheme
    MAIN_FILL   = '#d6e9f8'   # light blue fill for main boxes
    MAIN_EDGE   = '#2b6a9c'   # blue border
    EXCL_FILL   = '#fadbd8'   # light red fill for exclusion boxes
    EXCL_EDGE   = '#b8403b'   # red border
    DUP_FILL    = '#fdebd0'   # light orange for duplicate/removal box
    DUP_EDGE    = '#b87333'   # orange border
    INCL_FILL   = '#d5f5e3'   # light green for final inclusion
    INCL_EDGE   = '#1e8449'   # green border

    def draw_main_box(x, y, w, h, title, lines):
        """Blue main-stage box."""
        rect = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.12",
                              facecolor=MAIN_FILL, edgecolor=MAIN_EDGE, linewidth=2.0)
        ax.add_patch(rect)
        ax.text(x + w/2, y + h - 0.35, title, ha='center', va='top',
                fontsize=13, fontweight='bold', color='#1a5276')
        for li, line in enumerate(lines):
            ax.text(x + w/2, y + h - 0.9 - li*0.45, line, ha='center', va='top',
                    fontsize=10, color='#2c3e50')

    def draw_excl_box(x, y, w, h, title, lines):
        """Red exclusion box."""
        rect = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.12",
                              facecolor=EXCL_FILL, edgecolor=EXCL_EDGE, linewidth=1.8)
        ax.add_patch(rect)
        ax.text(x + w/2, y + h - 0.35, title, ha='center', va='top',
                fontsize=11, fontweight='bold', color='#7b241c')
        for li, line in enumerate(lines):
            ax.text(x + w/2, y + h - 0.85 - li*0.4, line, ha='center', va='top',
                    fontsize=9, color='#641e16')

    def draw_removal_box(x, y, w, h, text):
        """Orange removal-before-screening box."""
        rect = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.1",
                              facecolor=DUP_FILL, edgecolor=DUP_EDGE, linewidth=1.6)
        ax.add_patch(rect)
        ax.text(x + w/2, y + h/2, text, ha='center', va='center',
                fontsize=10.5, fontweight='bold', color='#7d3c0a')

    def draw_v_arrow(x, y_top, y_bot):
        ax.annotate('', xy=(x, y_bot), xytext=(x, y_top),
                    arrowprops=dict(arrowstyle='->', color='#555555', lw=2.2))

    def draw_h_arrow(x_left, x_right, y):
        ax.annotate('', xy=(x_right, y), xytext=(x_left, y),
                    arrowprops=dict(arrowstyle='->', color='#888888', lw=1.5))

    # ── Layout coordinates ──
    LEFT_X = 0.8
    MAIN_W = 8.0
    RIGHT_X = 10.0
    EXCL_W = 3.5

    # ── IDENTIFICATION (top) ──
    ID_Y = 19.0; ID_H = 2.2
    draw_main_box(LEFT_X, ID_Y, MAIN_W, ID_H, 'Identification of studies via databases',
        ['Records identified from:',
         '  Scopus (n = 312)    Web of Science (n = 187)    Google Scholar (n = 94)',
         'Total records identified (n = 593)'])

    draw_v_arrow(LEFT_X + MAIN_W/2, ID_Y, ID_Y - 0.4)

    # ── DUPLICATES REMOVED ──
    DUP_Y = 17.6; DUP_H = 0.7
    draw_removal_box(LEFT_X, DUP_Y, MAIN_W, DUP_H,
                     'Records removed before screening:  Duplicate records (n = 142)')

    draw_v_arrow(LEFT_X + MAIN_W/2, DUP_Y, DUP_Y - 0.4)

    # ── SCREENING ──
    SCR_Y = 14.0; SCR_H = 2.8
    draw_main_box(LEFT_X, SCR_Y, MAIN_W, SCR_H, 'Screening',
        ['Records screened by title & abstract',
         '(n = 451)'])

    # Screening exclusion branch
    SCR_EX_Y = 14.8; SCR_EX_H = 1.8
    draw_excl_box(RIGHT_X, SCR_EX_Y, EXCL_W, SCR_EX_H,
                  'Records excluded',
                  ['(n = 287)',
                   '· Wrong topic scope',
                   '· Non-peer-reviewed',
                   '· Non-English language'])
    draw_h_arrow(LEFT_X + MAIN_W, RIGHT_X, SCR_Y + SCR_H/2)

    draw_v_arrow(LEFT_X + MAIN_W/2, SCR_Y, SCR_Y - 0.4)

    # ── ELIGIBILITY ──
    ELIG_Y = 10.0; ELIG_H = 3.2
    draw_main_box(LEFT_X, ELIG_Y, MAIN_W, ELIG_H, 'Eligibility',
        ['Full-text articles assessed for eligibility',
         '(n = 164)'])

    # Eligibility exclusion branch
    ELIG_EX_Y = 8.5; ELIG_EX_H = 4.5
    draw_excl_box(RIGHT_X, ELIG_EX_Y, EXCL_W, ELIG_EX_H,
                  'Reports excluded',
                  ['(n = 114)',
                   '· Not ML/CV-based (n = 38)',
                   '· Not educ./surveillance (n = 31)',
                   '· Pre-2022 low relevance (n = 22)',
                   '· Full text not accessible (n = 15)',
                   '· Conference abstracts only (n = 8)'])
    draw_h_arrow(LEFT_X + MAIN_W, RIGHT_X, ELIG_Y + ELIG_H/2)

    draw_v_arrow(LEFT_X + MAIN_W/2, ELIG_Y, ELIG_Y - 0.4)

    # ── INCLUDED ──
    INCL_Y = 7.2; INCL_H = 1.5
    rect = FancyBboxPatch((LEFT_X, INCL_Y), MAIN_W, INCL_H, boxstyle="round,pad=0.12",
                          facecolor=INCL_FILL, edgecolor=INCL_EDGE, linewidth=2.0)
    ax.add_patch(rect)
    ax.text(LEFT_X + MAIN_W/2, INCL_Y + INCL_H - 0.45, 'Included',
            ha='center', va='top', fontsize=13, fontweight='bold', color='#145a32')
    ax.text(LEFT_X + MAIN_W/2, INCL_Y + 0.4,
            'Studies included in review (n = 50)',
            ha='center', va='center', fontsize=11, color='#1e8449', fontweight='bold')

    # ── Section labels on left side ──
    for y_pos, label in [(ID_Y + ID_H/2, 'IDENTIFICATION'),
                          (SCR_Y + SCR_H/2, 'SCREENING'),
                          (ELIG_Y + ELIG_H/2, 'ELIGIBILITY'),
                          (INCL_Y + INCL_H/2, 'INCLUDED')]:
        ax.text(0.2, y_pos, label, ha='center', va='center',
                fontsize=9, fontweight='bold', color='#888888', rotation=90)

    fig.tight_layout(pad=1.0)

    fig.savefig(os.path.join(OUTPUT_DIR, 'prisma_diagram.png'),
                dpi=200, bbox_inches='tight', facecolor='white', edgecolor='none')
    fig.savefig(os.path.join(PAPER_DIRS['prisma'], 'prisma_diagram.png'),
                dpi=200, bbox_inches='tight', facecolor='white', edgecolor='none')
    plt.close(fig)
    print("  -> prisma_diagram.png")

viz8_prisma()

print("\nAll 8 visualizations generated successfully!")
print(f"  Backup copies: {OUTPUT_DIR}/")
print(f"  Paper figures:  paper/Prisma/  paper/Citespace/  paper/VOSViewer/")

#!/usr/bin/env python3
"""Build the master's-student work schedule (график работы магистранта) document.

Reproduces the layout of the source template (A4, Times New Roman, 3 cm / 1.5 cm
margins, Astana IT University header with logo and double rule) for the
2026-2027 academic year, filled in with the dissertation topic of Akhmetov Medet
(computer vision / ML for detecting safety violations in educational institutions).

The header logo and the double rule are cropped from the source PDF at 600 dpi
so the rebuilt document is visually identical to the original.

Usage: python build_graphic.py
Output: График_работы_магистранта_Ахметов_Медет.docx (+ .pdf via Word, see convert step)
"""

from pathlib import Path

import fitz  # PyMuPDF
from docx import Document
from docx.shared import Pt, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
from docx.enum.table import WD_ALIGN_VERTICAL
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

HERE = Path(__file__).resolve().parent
SOURCE_PDF = HERE / "График_работы_магистранта_Гибрат_1.pdf"
ASSETS = HERE / "assets"
OUT_DOCX = HERE / "График_работы_магистранта_Ахметов_Медет.docx"

FONT = "Times New Roman"

# ---------------------------------------------------------------- content ---

STUDENT = "Ахметов Медет"
SUPERVISOR = "Башеева Жулдыз"
DEAN = "Адамова А.Д."
ROOM = "1.3.354"

# (№ of trimester, label, [(task, date), ...])
TRIMESTERS = [
    (1, "1 триместр (10 часов)", [
        ("Подготовительный этап практики (07.09–13.09.2026): постановка задач, "
         "согласование программы и календарного плана; уточнение гипотез; замысел "
         "статьи для журнала Scopus и выбор журнала", "07.09.2026"),
        ("Теоретико-аналитический этап (14.09–27.09.2026): обновление обзора "
         "литературы; система метрик детекции и оценки моделей; таксономия нарушений "
         "безопасности и признаков сцены", "21.09.2026"),
        ("Работа с данными (28.09–04.10.2026) и начало экспериментального этапа: "
         "наборы видеоданных и протокол разметки; экспериментальный стенд и "
         "baseline-модели", "05.10.2026"),
        ("Экспериментальный этап (05.10–25.10.2026): пространственно-временные модели "
         "детекции; анализ точности и задержки вывода (mAP, F1, latency); результаты "
         "для статьи", "19.10.2026"),
        ("Подготовка публикации (26.10–08.11.2026) и отчётный этап (09.11–14.11.2026): "
         "разбор черновика статьи для журнала Scopus; итоговый отчёт по практике, "
         "подготовка к защите", "09.11.2026"),
    ]),
    (2, "2 триместр (10 часов)", [
        ("Доработка статьи по результатам экспериментального исследования по "
         "замечаниям научного руководителя; оформление по требованиям журнала Scopus",
         "07.12.2026"),
        ("Финальная вычитка и подача статьи в журнал Scopus (срок завершения — "
         "до 31.12.2026)", "21.12.2026"),
        ("Постановка задач НИРМ на 5-й триместр; ответы на замечания рецензентов "
         "по статье (при получении)", "11.01.2027"),
        ("Дополнительные эксперименты по замечаниям рецензентов; кросс-доменная "
         "проверка моделей", "25.01.2027"),
        ("Отчёт по НИРМ за 5-й триместр; включение результатов статьи в структуру "
         "диссертации", "08.02.2027"),
    ]),
    (3, "3 триместр (15 часов)", [
        ("Постановка задач 3-го триместра; план завершения диссертационной работы",
         "15.03.2027"),
        ("Статус публикации; доработка рукописи по рецензии (при необходимости)",
         "29.03.2027"),
        ("Программный прототип системы обнаружения нарушений безопасности; постановка "
         "задач реализации", "12.04.2027"),
        ("Теоретико-методологическая глава: структура, логика изложения, полнота "
         "литературной базы", "26.04.2027"),
        ("Методическая глава: описание данных, моделей, метрик и процедуры анализа",
         "03.05.2027"),
        ("Апробация прототипа; интерпретация результатов", "17.05.2027"),
        ("Формулировка выводов диссертации; ограничения работы", "24.05.2027"),
        ("Сведение полного текста диссертации; антиплагиат, подготовка к защите",
         "31.05.2027"),
    ]),
]

COLUMNS = [
    ("№", 20.0),
    ("Триместр", 56.0),
    ("Направление работы / задачи", 186.0),
    ("Дата", 60.0),
    ("Аудитория", 60.0),
    ("Форма\nработы", 85.2),
]
TABLE_WIDTH = sum(w for _, w in COLUMNS)  # 467.2 pt = the 16.5 cm text column

BODY_SIZE = 11.0     # table body / header row font size
OUTER_SIZE = 12.0    # everything outside the table

# ------------------------------------------------------------- header art ---


def extract_assets():
    """Crop the university logo and the double rule out of the source PDF."""
    ASSETS.mkdir(exist_ok=True)
    doc = fitz.open(SOURCE_PDF)
    page = doc[0]
    # logo mark + wordmark; bbox taken from the source page geometry
    logo_rect = fitz.Rect(255.0, 35.0, 383.0, 103.0)
    rule_rect = fitz.Rect(63.44, 120.3, 545.36, 126.3)
    page.get_pixmap(clip=logo_rect, dpi=600).save(ASSETS / "logo.png")
    page.get_pixmap(clip=rule_rect, dpi=600).save(ASSETS / "rule.png")
    return logo_rect, rule_rect


# ------------------------------------------------------------ docx helpers ---


def set_run(run, size=OUTER_SIZE, bold=False):
    run.font.name = FONT
    run.font.size = Pt(size)
    run.font.bold = bold
    rpr = run._element.get_or_add_rPr()
    rfonts = rpr.find(qn("w:rFonts"))
    if rfonts is None:
        rfonts = OxmlElement("w:rFonts")
        rpr.insert(0, rfonts)
    for attr in ("w:ascii", "w:hAnsi", "w:cs", "w:eastAsia"):
        rfonts.set(qn(attr), FONT)


def style_par(par, size=OUTER_SIZE, bold=False, align=None, space_after=0,
              space_before=0, left_indent=None, spacing=None):
    pf = par.paragraph_format
    pf.space_after = Pt(space_after)
    pf.space_before = Pt(space_before)
    if spacing is not None:
        pf.line_spacing = Pt(spacing)
    if left_indent is not None:
        pf.left_indent = Pt(left_indent)
    if align is not None:
        par.alignment = align
    for run in par.runs:
        set_run(run, size, bold)
    return par


def add_par(container, lines, size=OUTER_SIZE, bold=False, align=None,
            space_after=0, space_before=0, left_indent=None, spacing=None):
    """Add a paragraph; `lines` is a list rendered as soft line breaks."""
    if isinstance(lines, str):
        lines = [lines]
    par = container.add_paragraph()
    for i, line in enumerate(lines):
        run = par.add_run(line)
        set_run(run, size, bold)
        if i != len(lines) - 1:
            run.add_break()
    style_par(par, size, bold, align, space_after, space_before, left_indent, spacing)
    return par


def shade(cell, fill):
    tcpr = cell._tc.get_or_add_tcPr()
    el = OxmlElement("w:shd")
    el.set(qn("w:val"), "clear")
    el.set(qn("w:color"), "auto")
    el.set(qn("w:fill"), fill)
    tcpr.append(el)


def no_wrap_tight(cell, margin=2.0):
    """Reduce default cell padding so more text fits per line."""
    tcpr = cell._tc.get_or_add_tcPr()
    mar = OxmlElement("w:tcMar")
    for side in ("top", "start", "bottom", "end"):
        el = OxmlElement(f"w:{side}")
        el.set(qn("w:w"), str(int(margin * 20)))  # twips
        el.set(qn("w:type"), "dxa")
        mar.append(el)
    tcpr.append(mar)


def cant_split(row):
    trpr = row._tr.get_or_add_trPr()
    el = OxmlElement("w:cantSplit")
    trpr.append(el)


def table_borders(table, sz=4):
    tblpr = table._tbl.tblPr
    borders = OxmlElement("w:tblBorders")
    for edge in ("top", "left", "bottom", "right", "insideH", "insideV"):
        el = OxmlElement(f"w:{edge}")
        el.set(qn("w:val"), "single")
        el.set(qn("w:sz"), str(sz))
        el.set(qn("w:space"), "0")
        el.set(qn("w:color"), "000000")
        borders.append(el)
    tblpr.append(borders)


def fixed_layout(table, total_pt):
    """Pin the table to an exact width; without tblW Word re-fits the columns."""
    tblpr = table._tbl.tblPr
    for tag in ("w:tblW", "w:tblLayout"):
        for old in tblpr.findall(qn(tag)):
            tblpr.remove(old)
    width = OxmlElement("w:tblW")
    width.set(qn("w:w"), str(int(round(total_pt * 20))))  # twips
    width.set(qn("w:type"), "dxa")
    tblpr.append(width)
    el = OxmlElement("w:tblLayout")
    el.set(qn("w:type"), "fixed")
    tblpr.append(el)


def cell_text(cell, lines, size=BODY_SIZE, bold=False, align=WD_ALIGN_PARAGRAPH.CENTER):
    cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
    par = cell.paragraphs[0]
    if isinstance(lines, str):
        lines = [lines]
    for i, line in enumerate(lines):
        run = par.add_run(line)
        set_run(run, size, bold)
        if i != len(lines) - 1:
            run.add_break()
    style_par(par, size, bold, align)
    no_wrap_tight(cell)
    return par


# ------------------------------------------------------------------ build ---


def build():
    logo_rect, rule_rect = extract_assets()
    doc = Document()

    normal = doc.styles["Normal"]
    normal.font.name = FONT
    normal.font.size = Pt(OUTER_SIZE)
    # Word's default is 1.15 line spacing with 8 pt after; the template uses single
    normal.paragraph_format.line_spacing = 1.0
    normal.paragraph_format.space_after = Pt(0)
    normal.paragraph_format.space_before = Pt(0)
    rpr = normal.element.get_or_add_rPr()
    rfonts = rpr.find(qn("w:rFonts"))
    if rfonts is None:
        rfonts = OxmlElement("w:rFonts")
        rpr.insert(0, rfonts)
    for attr in ("w:ascii", "w:hAnsi", "w:cs", "w:eastAsia"):
        rfonts.set(qn(attr), FONT)

    sec = doc.sections[0]
    sec.page_width = Cm(21.0)
    sec.page_height = Cm(29.7)
    sec.left_margin = Cm(3.0)
    sec.right_margin = Cm(1.5)
    sec.top_margin = Cm(2.0)
    sec.bottom_margin = Cm(2.0)
    sec.header_distance = Cm(1.8)
    sec.footer_distance = Cm(1.25)
    # the letterhead appears on page 1 only, as in the source document
    sec.different_first_page_header_footer = True
    sec.header.paragraphs[0].text = ""

    # ------------------------------------------------------- page header ---
    header = sec.first_page_header
    ht = header.add_table(rows=1, cols=3, width=Pt(TABLE_WIDTH))
    ht.autofit = False
    widths = (155.0, 160.0, 152.2)
    fixed_layout(ht, TABLE_WIDTH)
    for i, w in enumerate(widths):
        ht.columns[i].width = Pt(w)
        ht.cell(0, i).width = Pt(w)
    hcells = ht.rows[0].cells
    for c in hcells:
        no_wrap_tight(c)
    cell_text(hcells[0], ["«Astana IT University»", "жауапкершілігі шектеулі",
                          "серіктестігі"], size=OUTER_SIZE, bold=True,
              align=WD_ALIGN_PARAGRAPH.LEFT)
    cell_text(hcells[2], ["«Astana IT University»", "Limited Liability",
                          "Partnership"], size=OUTER_SIZE, bold=True,
              align=WD_ALIGN_PARAGRAPH.RIGHT)
    hcells[1].vertical_alignment = WD_ALIGN_VERTICAL.CENTER
    logo_par = hcells[1].paragraphs[0]
    logo_par.alignment = WD_ALIGN_PARAGRAPH.CENTER
    logo_par.add_run().add_picture(str(ASSETS / "logo.png"),
                                   width=Pt(logo_rect.width), height=Pt(logo_rect.height))

    rule_par = header.add_paragraph()
    rule_par.alignment = WD_ALIGN_PARAGRAPH.LEFT
    rule_par.paragraph_format.left_indent = Pt(rule_rect.x0 - 85.04)  # 85.04pt = 3 cm
    rule_par.paragraph_format.space_before = Pt(4)
    rule_par.paragraph_format.space_after = Pt(0)
    rule_par.add_run().add_picture(str(ASSETS / "rule.png"),
                                   width=Pt(rule_rect.width), height=Pt(rule_rect.height))
    # drop the placeholder paragraph Word leaves above the letterhead table
    first_par = header.paragraphs[0]
    if not first_par.text.strip() and not first_par._element.findall(qn("w:r")):
        first_par._element.getparent().remove(first_par._element)

    # ------------------------------------------------------------- body ---
    add_par(doc, ["УТВЕРЖДАЮ", "Декан Школы", "программной инженерии",
                  "Astana IT University", f"___________ {DEAN}",
                  "«____» ____________ 2026 г."],
            bold=True, align=WD_ALIGN_PARAGRAPH.LEFT,
            left_indent=354.3 - 85.04, space_after=14)

    add_par(doc, ["ГРАФИК РАБОТЫ МАГИСТРАНТА С НАУЧНЫМ РУКОВОДИТЕЛЕМ",
                  "на 2026–2027 учебный год"],
            bold=True, align=WD_ALIGN_PARAGRAPH.CENTER,
            space_before=14, space_after=14)

    add_par(doc, f"ФИО магистранта: {STUDENT}", align=WD_ALIGN_PARAGRAPH.LEFT,
            space_after=10)
    add_par(doc, f"ФИО научного руководителя: {SUPERVISOR}",
            align=WD_ALIGN_PARAGRAPH.LEFT, space_before=0, space_after=10)

    def new_table(n_rows):
        t = doc.add_table(rows=n_rows, cols=len(COLUMNS))
        t.autofit = False
        fixed_layout(t, TABLE_WIDTH)
        table_borders(t)
        for i, (_, w) in enumerate(COLUMNS):
            t.columns[i].width = Pt(w)
        return t

    def fill_row(table, r, task=None, date=None):
        cells = table.rows[r].cells
        for j, text in enumerate([None, None, task, date, ROOM, "Консультация"]):
            if text is not None:
                cell_text(cells[j], text)
            cells[j].width = Pt(COLUMNS[j][1])
        cant_split(table.rows[r])

    def fill_block(table, first, last, tri_no, tri_label):
        """Merge the № and Триместр columns over one whole trimester block."""
        num_cell = table.cell(first, 0).merge(table.cell(last, 0))
        tri_cell = table.cell(first, 1).merge(table.cell(last, 1))
        cell_text(num_cell, str(tri_no))
        cell_text(tri_cell, tri_label.replace(" (", "\n(").split("\n"))
        for j in (0, 1, 2, 3, 4, 5):
            table.cell(first, j).width = Pt(COLUMNS[j][1])

    # ---- table 1: column headings + first trimester (page 1) ----
    t1 = new_table(1 + len(TRIMESTERS[0][2]))
    for i, (title, _) in enumerate(COLUMNS):
        cell_text(t1.rows[0].cells[i], title.split("\n"), size=BODY_SIZE, bold=True)
        t1.rows[0].cells[i].width = Pt(COLUMNS[i][1])
    cant_split(t1.rows[0])
    for n, (task, date) in enumerate(TRIMESTERS[0][2]):
        fill_row(t1, 1 + n, task, date)
    fill_block(t1, 1, len(TRIMESTERS[0][2]), TRIMESTERS[0][0], TRIMESTERS[0][1])

    # second and third trimesters continue on a new page, as in the template
    break_par = doc.add_paragraph()
    break_par.add_run().add_break(WD_BREAK.PAGE)
    style_par(break_par, space_after=0, spacing=1)

    t2 = new_table(sum(len(rows) for _, _, rows in TRIMESTERS[1:]) + 1)
    r = 0
    for tri_no, tri_label, rows in TRIMESTERS[1:]:
        first = r
        for task, date in rows:
            fill_row(t2, r, task, date)
            r += 1
        fill_block(t2, first, r - 1, tri_no, tri_label)

    total_cells = t2.rows[r].cells
    merged = t2.cell(r, 0).merge(t2.cell(r, 4))
    cell_text(merged, "Всего", size=OUTER_SIZE, bold=True)
    cell_text(total_cells[5], "35 часов", size=OUTER_SIZE, bold=True)
    t2.cell(r, 5).width = Pt(COLUMNS[5][1])
    cant_split(t2.rows[r])

    add_par(doc, f"Магистрант: {STUDENT} / ____________________", bold=True,
            align=WD_ALIGN_PARAGRAPH.LEFT, space_before=28, space_after=14)
    add_par(doc, f"Научный руководитель: {SUPERVISOR} / _____________________",
            bold=True, align=WD_ALIGN_PARAGRAPH.LEFT)

    doc.save(OUT_DOCX)
    print(f"written: {OUT_DOCX}")


if __name__ == "__main__":
    build()

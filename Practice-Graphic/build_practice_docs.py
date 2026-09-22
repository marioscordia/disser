#!/usr/bin/env python3
"""Rebuild the research-practice document set for Akhmetov Medet.

The source document set (7 pages: title page, 10-week calendar plan, practice
programme, supervisor's review) belongs to a groupmate.  Rather than rebuilding
the layout, this script edits a copy of the original DOCX in place — the
formatting, styles, tables and page breaks are inherited unchanged — and only
replaces the student name, the dissertation topic and the topic-specific cells
(weekly tasks and practice stages) with text matching Akhmetov Medet's
dissertation: computer vision / ML models for detecting safety violations and
child abuse in educational institutions.

Usage: python build_practice_docs.py
Output: Документы_по_исследовательской_практике_Ахметов_Медет.docx (+ .pdf via Word)
"""

import copy
import shutil
from pathlib import Path

import docx
from docx.oxml.ns import qn

HERE = Path(__file__).resolve().parent
SRC = HERE / "Документы_по_исследовательской_практике_Гибрат.docx"
OUT = HERE / "Документы_по_исследовательской_практике_Ахметов_Медет.docx"

OLD_NAME = "Гибрат Ержан"
NEW_NAME = "Ахметов Медет"

TOPIC = ("Компьютерное зрение и модели машинного обучения для обнаружения "
         "нарушений безопасности и жестокого обращения с детьми в "
         "образовательных учреждениях")

# --------------------------------------------------------------- content ---
# Weeks 1-8 of the calendar plan (table 0, rows 1-8):
# (activity, concrete tasks, expected results).  None keeps the source text.
WEEKS = {
    1: (None,
        "Согласовать задачи практики в рамках 4-го триместра; уточнить "
        "исследовательские вопросы и гипотезы по итогам систематического "
        "библиометрического обзора (дефицит детских наборов данных, отсутствие "
        "privacy-aware решений); сформулировать замысел статьи по результатам "
        "эксперимента для журнала Scopus и выбрать целевой журнал",
        None),
    2: (None,
        "Дополнить обзор смежными направлениями: лёгкие (edge-deployable) "
        "архитектуры детекции, privacy-preserving компьютерное зрение, детские "
        "наборы данных; публикации 2025–2026 в Scopus / WoS",
        None),
    3: ("Формализация системы метрик и признаков сцены",
        "Определить метрики детекции (mAP@0.5, precision, recall, F1, "
        "AUC-ROC) и эксплуатационные метрики (задержка инференса, FPS); "
        "классифицировать признаки сцены и контекста (плотность людей, ракурс, "
        "время суток)",
        "Методологическая записка: формальные определения метрик, таксономия "
        "признаков сцены и контекста; раздел Methodology статьи"),
    4: (None,
        "Отобрать публичные наборы видеоданных для детекции насилия и аномалий "
        "(RWF-2000, UCF-Crime, XD-Violence); спроектировать протокол разметки и "
        "разбиения выборки; предобработка кадров",
        None),
    5: ("Базовые модели детекции",
        "Реализовать базовые (baseline) модели: 3D-CNN, I3D, SlowFast, "
        "детекторы YOLO-семейства; собрать экспериментальный стенд с "
        "фиксированными разбиениями и сидами",
        "Воспроизводимый стенд; таблица метрик детекции baseline-моделей"),
    6: ("Пространственно-временные модели детекции",
        "Реализовать и обучить пространственно-временные модели детекции "
        "насилия и аномального поведения (двухпоточные сети, "
        "видео-трансформеры, лёгкие мобильные архитектуры); сравнить с "
        "baseline по метрикам детекции",
        "Обученные модели; сравнительная таблица mAP / F1 / AUC-ROC с "
        "доверительными интервалами"),
    7: ("Анализ точности и устойчивости моделей",
        "Оценить точность и задержку вывода моделей на edge-устройствах; "
        "провести кросс-доменную проверку (разные школы, ракурсы, освещение); "
        "проанализировать ложные срабатывания; проверить устойчивость "
        "результатов (bootstrap)",
        "Таблицы и графики метрик; результаты статистических тестов; раздел "
        "Results статьи"),
}

# Practice programme (table 2, rows 1-6): row -> (stage name, content, note)
PROGRAMME = {
    2: (None,
        "Обновление обзора научной литературы по теме диссертации (лёгкие "
        "архитектуры детекции, privacy-preserving компьютерное зрение, "
        "мультимодальная фузия, детские наборы данных); формализация системы "
        "метрик детекции и локализации; таксономия нарушений безопасности и "
        "признаков сцены",
        None),
    3: (None,
        "Отбор публичных наборов видеоданных для детекции насилия и аномалий "
        "(RWF-2000, UCF-Crime, XD-Violence); разработка протокола разметки и "
        "разбиения выборки; предобработка кадров и аугментация",
        None),
    4: (None,
        "Реализация baseline и пространственно-временных моделей детекции; "
        "сравнение по метрикам точности и задержки вывода; анализ ошибок и "
        "кросс-доменная проверка; оценка устойчивости результатов",
        None),
}


# --------------------------------------------------------------- helpers ---


def para_text(par):
    return "".join(r.text for r in par.runs)


def replace_in_paragraph(par, old, new):
    """Replace `old` with `new` in a paragraph, keeping each run's formatting."""
    runs = par.runs
    full = "".join(r.text for r in runs)
    if old not in full:
        return False
    while old in full:
        idx = full.index(old)
        end = idx + len(old)
        # locate the runs holding the start and the end of the match
        pos, start_run = 0, None
        for r in runs:
            if start_run is None and pos + len(r.text) > idx:
                start_run, start_off = r, idx - pos
            if pos + len(r.text) >= end:
                end_run, end_off = r, end - pos
                break
            pos += len(r.text)
        else:  # pragma: no cover - defensive
            return False
        if start_run is end_run:
            start_run.text = (start_run.text[:start_off] + new
                              + start_run.text[end_off:])
        else:
            start_run.text = start_run.text[:start_off] + new
            end_run.text = end_run.text[end_off:]
            for r in runs[runs.index(start_run) + 1:runs.index(end_run)]:
                r.text = ""
        full = "".join(r.text for r in runs)
    return True


def set_paragraph_text(par, text):
    """Replace a paragraph's whole text, keeping the first run's formatting."""
    runs = par.runs
    rpr = None
    if runs:
        found = runs[0]._element.find(qn("w:rPr"))
        rpr = copy.deepcopy(found) if found is not None else None
    for r in runs:
        r._element.getparent().remove(r._element)
    run = par.add_run(text)
    if rpr is not None:
        run._element.insert(0, rpr)


def set_cell_text(cell, text):
    """Replace a table cell's content with a single paragraph."""
    pars = cell.paragraphs
    keep = next((p for p in pars if para_text(p).strip()), pars[0])
    for p in pars:
        if p is not keep:
            p._element.getparent().remove(p._element)
    set_paragraph_text(keep, text)


def each_paragraph(document):
    """Yield every paragraph in the document body and in all tables."""
    for par in document.paragraphs:
        yield par
    for table in document.tables:
        for row in table.rows:
            seen = set()
            for cell in row.cells:
                if cell._tc in seen:
                    continue
                seen.add(cell._tc)
                for par in cell.paragraphs:
                    yield par


# ------------------------------------------------------------------ main ---


def build():
    shutil.copyfile(SRC, OUT)
    doc = docx.Document(OUT)

    # 1. student name everywhere (title page, headers of each section, signatures)
    for par in each_paragraph(doc):
        replace_in_paragraph(par, OLD_NAME, NEW_NAME)

    # 2. dissertation topic on the title page
    for par in doc.paragraphs:
        if par.text.startswith("Тема магистерской диссертации:"):
            set_paragraph_text(par, f"Тема магистерской диссертации: {TOPIC}")

    # the topic runs one line longer than the source's, so drop trailing blank
    # lines on the title page — otherwise "Астана 2026" is pushed onto page 2
    pars = doc.paragraphs
    last = next(i for i, p in enumerate(pars) if p.text.strip() == "Астана 2026")
    removed = 0
    while removed < 3 and last - 1 >= 0 and not pars[last - 1].text.strip():
        pars[last - 1]._element.getparent().remove(pars[last - 1]._element)
        pars = doc.paragraphs
        last = next(i for i, p in enumerate(pars)
                    if p.text.strip() == "Астана 2026")
        removed += 1

    # 3. weekly plan: weeks 1-8 in table 0, rows 1-8
    t0 = doc.tables[0]
    for row_idx, (activity, tasks, results) in WEEKS.items():
        cells = t0.rows[row_idx].cells
        for col, value in ((1, activity), (2, tasks), (3, results)):
            if value is not None:
                set_cell_text(cells[col], value)

    # 4. practice programme: content of stages 2-4 in table 2
    t2 = doc.tables[2]
    for row_idx, (name, content, note) in PROGRAMME.items():
        cells = t2.rows[row_idx].cells
        for col, value in ((1, name), (3, content), (4, note)):
            if value is not None:
                set_cell_text(cells[col], value)

    doc.save(OUT)
    print(f"written: {OUT}")


if __name__ == "__main__":
    build()

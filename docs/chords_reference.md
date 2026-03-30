# Справочник аккордов (актуальный)

Источник истины: `config/boards/shields/PNCATEHO/chords.dtsi`.

## Семантика вариантов

- **base** — обычный аккорд без thumbs.
- **curved** — аккорд + `LIT/RIT`.
- **splayed** — аккорд + `LOT/ROT`.
- **both** — аккорд + оба thumbs.

## Используемые макросы

- `TCOMBO(...)` — base + curved + splayed + both.
- `TCOMBO_NO_BASE(...)` — только curved/splayed/both.
- `TCOMBO_NO_BASE_LAYERS(...)` — слой-ограниченный вариант без base.
- `TCOMBO_ONLY_BASE_LAYERS(...)` — только base (зеркально на обе руки).
- `TCOMBO_ONLY_BASE_LAYERS_IDLE(...)` — only-base + `require-prior-idle-ms`.

## Ключевые одно-клавишные `TCOMBO_NO_BASE` (RU/ENG слои)

| Аккорд | Curved | Splayed | Both |
| :--- | :--- | :--- | :--- |
| `b` (`TLP`/`TRP`) | `LEFT` | `Shift+B` | `Shift+LEFT` |
| `j` (`TLI`/`TRI`) | `RIGHT` | `Shift+J` | `Shift+RIGHT` |
| `h` (`BLP`/`BRP`) | `Sticky GUI` | `Shift+H` | `HOME` |
| `y` (`BLI`/`BRI`) | `Sticky Shift` | `Shift+Y` | `END` |
| `f` (`TLR`/`TRR`) | `UP` | `Shift+F` | `Shift+UP` |
| `c` (`BLR`/`BRR`) | `Sticky Alt` | `Shift+C` | `PG_UP` |

`n` задан через `TCOMBO`, но тоже дает sticky-модификатор: `splayed = Sticky Ctrl`.

## Слой-специфичные группы

- **Переключение языка:** `lang_ru`, `lang_en` (`TCOMBO_ONLY_BASE_LAYERS`).
- **HOLD_NUM_L:**
  - only-base: `num_8`, `num_7`, `num_9`
  - no-base: `num_2`, `num_1`, `num_5`, `num_4`
- **HOLD_SYM_L:** `sym_at`, `sym_lpar`, `sym_rpar`, `sym_hash`, `sym_quest`, `sym_slash`
- **HOLD_NAV_L:** `nav_up`, `nav_left`, `nav_down`, `nav_right`
- **HOLD_BRACKETS_L:** `hb_dquote`, `hb_apos`, `hb_pipe`
- **HOLD_TYPO_L:** `ht_pipe`, `ht_tilde`
- **HOLD_MEDIA_L:** `hm_shot_screen`, `hm_joxi`

## Lock-комбо (toggle)

- `lock_nav`: `TCOMBO_ONLY_BASE_LAYERS_IDLE(..., &tog NAV_L, ..., 150)`
- `lock_mouse`: `TCOMBO_ONLY_BASE_LAYERS_IDLE(..., &tog MOUSE_L, ..., 150)`

`150 ms` idle-порог снижает ложные активации при печати.

## Примечание по полноте

В файле `chords.dtsi` также определен полный набор букв/символов/функциональных аккордов (`TCOMBO(d..boot/bt)`).
Для изменений корректнее редактировать именно `chords.dtsi`, а этот файл использовать как карту по группам и семантике.

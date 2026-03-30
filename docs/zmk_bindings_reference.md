# ZMK: справочник биндингов в текущем конфиге PNCATEHO

Актуально для:

- `config/boards/shields/PNCATEHO/PNCATEHO.keymap`
- `config/boards/shields/PNCATEHO/chords.dtsi`
- `config/boards/shields/PNCATEHO/custom_behaviors.dtsi`
- `config/boards/shields/PNCATEHO/custom_macros.dtsi`
- `config/boards/shields/PNCATEHO/chord_macros.dtsi`

## 1) Базовые behavior-узлы

- `&kp KEY` — отправка keycode.
- `&lt LAYER KEY` — layer-tap: tap = `KEY`, hold = включение `LAYER`.
- `&trans` — прозрачный биндинг.
- `&none` — пустой биндинг.
- `&sk MOD` — sticky-модификатор.
- `&to LAYER` — безусловный переход на слой.
- `&tog LAYER` — переключение состояния слоя.

Глобальные настройки `&sk` заданы в `PNCATEHO.keymap`:

- `release-after-ms = <STICKY_TIMEOUT>;`
- `quick-release;`

## 2) Мышь, BT, питание

- `&mmv MOVE_*` — движение курсора.
- `&msc SCRL_*` — вертикальный скролл.
- `&mkp LCLK|RCLK` — кнопки мыши.
- `&bt BT_SEL N` / `&bt BT_CLR` — выбор и очистка BT-профилей.
- `&bootloader` — вход в загрузчик.
- `&ext_power EP_OFF` — отключение внешнего питания.

## 3) Пользовательские macro/behavior-узлы

Определены через include-файлы:

- `custom_macros.dtsi`: `&mg_dot`, `&mg_comma`, `&mac_to_en`, `&mac_to_ru`
- `custom_behaviors.dtsi`: `&td_bkt`, `&td_ang`, `&td_brc`, `&ht_*`, `&sym_*_mm`

Ключевые группы:

- `&sym_*_mm` — 4-состояния через `MOD_MPH` (base/cmd/shift/cmd+shift).
- `&td_*` — tap-dance для скобок.
- `&ht_curved`, `&ht_splayed` — универсальные hold-tap.
- `&ht_curved_mg`, `&ht_splayed_mg` — hold-tap с tap-макросами пунктуации.
- `&ht_combo_ru`, `&ht_combo_en` — hold-tap с языковыми макросами.

## 4) Модификаторные обертки keycode

- `LS(X)` — Shift + `X`
- `LC(X)` — Ctrl + `X`
- `LA(X)` — Alt + `X`
- `LG(X)` — GUI/Cmd + `X`
- `RA(X)` — Right Alt + `X`

Примеры вложений:

- `LS(RA(SLASH))`
- `LS(LC(LA(N1)))`

## 5) Комбо-макросы (актуальные имена)

Определены в `chord_macros.dtsi`:

- `TCOMBO(...)` — полный набор: base + curved + splayed + both.
- `TCOMBO_NO_BASE(...)` — только curved/splayed/both (без base).
- `TCOMBO_LAYERS(...)` — то же, что `TCOMBO`, но с явным `LAYERS`.
- `TCOMBO_NO_BASE_LAYERS(...)` — то же, что `TCOMBO_NO_BASE`, но с явным `LAYERS`.
- `TCOMBO_ONLY_BASE_LAYERS(...)` — только base (зеркально для левой/правой).
- `TCOMBO_ONLY_BASE_LAYERS_IDLE(...)` — как выше + `require-prior-idle-ms`.
- `MOD_MPH(...)` — генератор иерархии `behavior-mod-morph`.

Важно: `TCOMBO_ONLY_BASE_LAYERS(...)` концептуально действительно является “only base” парой к `TCOMBO_NO_BASE(...)`.

## 6) Поля combo-нод

- `timeout-ms` — окно распознавания аккорда.
- `key-positions` — позиции клавиш в аккорде.
- `layers` — список слоев, где комбо активно.
- `require-prior-idle-ms` — защита от ложных срабатываний в потоке печати.

## 7) Позиционные alias

Alias объявлены в `custom_variables.dtsi`:

- Левая половина: `TLP TLR TLM TLI`, `BLP BLR BLM BLI`, `LIT LOT`
- Правая половина: `TRP TRR TRM TRI`, `BRP BRR BRM BRI`, `RIT ROT`

## 8) Короткие примеры из текущего keymap

- `&lt HOLD_NUM_L B` — tap `B`, hold слой `HOLD_NUM_L`.
- `&ht_curved LGUI BSPC` — hold `LGUI`, tap `BSPC`.
- `TCOMBO_NO_BASE(b, &kp LEFT, &kp LS(B), &kp LS(LEFT), TLP, TRP)` — для `b`: curved = `LEFT`, splayed = `B`, both = `Shift+LEFT`.

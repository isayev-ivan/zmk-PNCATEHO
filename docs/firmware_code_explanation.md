# Разбор кода прошивки (актуальная структура)

## 1) Центр архитектуры: `PNCATEHO.keymap`

`config/boards/shields/PNCATEHO/PNCATEHO.keymap` — точка сборки всей логики:

- подключает `chord_macros.dtsi` и `custom_variables.dtsi`;
- внутри `/ { ... }` подключает:
  - `macros { #include "custom_macros.dtsi" }`
  - `combos { #include "chords.dtsi" }`
  - `behaviors { #include "custom_behaviors.dtsi" }`
- задает слои: `RU_L`, `ENG_L`, `NAV_L`, `MOUSE_L`, `HOLD_*`.

Отдельно в keymap настроены:

- `&mmv` и `&msc` (ускорение/профиль мыши),
- `&sk` (`release-after-ms = <STICKY_TIMEOUT>`, `quick-release`).

## 2) Переиспользование через `custom_*`

### `custom_variables.dtsi`

Содержит:

- таймауты (`COMBO_TIMEOUT`, `STICKY_TIMEOUT`);
- номера слоев (`RU_L..HOLD_TYPO_L`);
- keycode-алиасы (`SYM_*`);
- алиасы физических позиций (`TLP..BRI`, `LIT/LOT/RIT/ROT`).

### `custom_macros.dtsi`

Содержит:

- `mg_dot`, `mg_comma` (пунктуация + пробел);
- `mac_to_en`, `mac_to_ru` (переключение языка + переход на слой).

### `custom_behaviors.dtsi`

Содержит:

- `MOD_MPH(...)` для `sym_*_mm` (4 состояния: base/cmd/shift/cmd+shift);
- tap-dance: `td_bkt`, `td_ang`, `td_brc`;
- hold-tap: `ht_curved`, `ht_splayed`, `ht_*_mg`, `ht_combo_ru`, `ht_combo_en`.

## 3) Аккордовый движок: `chords.dtsi` + `chord_macros.dtsi`

`chord_macros.dtsi` — библиотека макросов-генераторов:

- `TCOMBO(...)`
- `TCOMBO_NO_BASE(...)`
- `TCOMBO_LAYERS(...)`
- `TCOMBO_NO_BASE_LAYERS(...)`
- `TCOMBO_ONLY_BASE_LAYERS(...)`
- `TCOMBO_ONLY_BASE_LAYERS_IDLE(...)`
- `MOD_MPH(...)`

`chords.dtsi` — конкретные определения аккордов на этих макросах:

- базовые буквы/символы;
- модификаторные аккорды;
- слой-специфичные аккорды (`HOLD_NUM_L`, `HOLD_SYM_L`, `HOLD_NAV_L`, ...);
- lock-комбо (`lock_nav`, `lock_mouse`) с `require-prior-idle-ms`.

## 4) Важный семантический момент

Пара имен:

- `TCOMBO_NO_BASE(...)` = только non-base варианты (curved/splayed/both),
- `TCOMBO_ONLY_BASE_LAYERS(...)` = только base-вариант.

Это согласованная терминология для противоположных сценариев.

## 5) Аппаратный слой

### `PNCATEHO.dtsi`

- `zmk,kscan = &kscan0`
- `zmk,matrix_transform = &default_transform`
- `kscan0` использует `zmk,kscan-gpio-direct`
- `default_transform` задает логическое отображение 3x8

### Overlay-файлы

- `PNCATEHO_left.overlay` — подключает `PNCATEHO.dtsi`.
- `PNCATEHO_right.overlay` — подключает `PNCATEHO.dtsi` и задает `col-offset = <10>`.

## 6) Kconfig-уровень

### Корневой `config/PNCATEHO.conf`

- глобальные опции пользователя;
- повышенные лимиты combo:
  - `CONFIG_ZMK_COMBO_MAX_COMBOS_PER_KEY=128`
  - `CONFIG_ZMK_COMBO_MAX_KEYS_PER_COMBO=10`
  - `CONFIG_ZMK_COMBO_MAX_PRESSED_COMBOS=10`

### Shield-уровень

- `config/boards/shields/PNCATEHO/PNCATEHO.conf` — дефолт щита (сон, мышь, питание, имя).
- `Kconfig.shield` — регистрация `PNCATEHO_left/right`.
- `Kconfig.defconfig` — `ZMK_SPLIT`, `ZMK_SPLIT_ROLE_CENTRAL` (левая половина).

## 7) Метаданные

`PNCATEHO.zmk.yml` описывает shield для инструментов сборки:

- `id: PNCATEHO`
- `type: shield`
- `requires: [pro_micro]`

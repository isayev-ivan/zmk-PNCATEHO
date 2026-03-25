# ZMK: что значит `&lt`, `&kp` и другие используемые штуки

Ниже — практический справочник именно по тому, что используется в:

- `config/boards/shields/PNCATEHO/PNCATEHO.keymap`
- `config/boards/shields/PNCATEHO/chords.dtsi`

## 1) Базовые поведения (behaviors)

- `&kp KEY` — отправить keycode.
  - Пример: `&kp A`, `&kp ENTER`, `&kp SYM_AT`.
- `&lt LAYER KEY` — layer-tap: удержание включает слой, тап отправляет `KEY`.
  - Пример: `&lt HOLD_SYM_L J`.
- `&trans` — прозрачная клавиша: взять действие с нижележащего слоя.
- `&none` — пусто: ничего не делать.
- `&sk MOD` — sticky-модификатор (модификатор «залипает» на следующее нажатие).
  - Глобальные параметры `&sk` задаются в keymap:
    - `release-after-ms = <N>` — максимальное время жизни залипания в мс.\
      Если после нажатия `&sk MOD` за `N` мс не нажать следующую клавишу, модификатор автоматически сбросится.
    - `quick-release` — отпускать sticky-модификатор сразу после первого модифицированного нажатия (one-shot поведение).
  - Практически это работает так:
    - нажал `&sk LSHIFT` → Shift «вооружен»;
    - нажал следующую клавишу (например `a`) → получаешь `A`;
    - из-за `quick-release` Shift сразу отключается и дальше печать обычная.
- `&to LAYER` — безусловно переключиться на слой.
- `&tog LAYER` — toggle слоя (вкл/выкл).

## 2) Мышь

- `&mmv DIRECTION` — движение курсора.
  - Примеры: `MOVE_UP`, `MOVE_LEFT`, `MOVE_RIGHT`, `MOVE_DOWN`.
- `&msc DIRECTION` — скролл.
  - Примеры: `SCRL_UP`, `SCRL_DOWN`.
- `&mkp BTN` — кнопка мыши.
  - Примеры: `LCLK`, `RCLK`.

## 3) Bluetooth / питание / спец-действия

- `&bt BT_SEL N` — выбрать BT-профиль `N`.
- `&bt BT_CLR` — очистить BT-связи.
- `&bootloader` — вход в bootloader.
- `&ext_power EP_OFF` — выключить внешнее питание.

## 4) Пользовательские behaviors и macros из keymap

Внутри `/ { macros { ... } }` и `/ { behaviors { ... } }` создаются локальные сущности, которые потом вызываются как `&имя`.

- Макросы:
  - `&mg_dot`, `&mg_comma` — макросы набора пунктуации.
  - `&mac_to_en`, `&mac_to_ru` — макросы смены языка.
- Behaviors:
  - `&ht_curved`, `&ht_splayed` — hold-tap для больших пальцев.
  - `&ht_combo_ru`, `&ht_combo_en` — hold-tap, где hold вызывает языковой макрос.
  - `&quest_excl`, `&bracket_left`, `&bracket_right`, и т.д. — mod-morph behaviors.
    - `mod-morph` — поведение «одна клавиша, два результата в зависимости от активных модификаторов».
    - В вашем keymap эти behaviors проверяют `Shift` (`mods = <(MOD_LSFT|MOD_RSFT)>`).
    - Если Shift не зажат, отправляется первый биндинг из `bindings = <A>, <B>`.
    - Если Shift зажат, отправляется второй биндинг.
    - Пример: `quest_excl` даёт `?` без Shift и `!` с Shift.
    - Пример: `bracket_left` даёт `(` без Shift и `<` с Shift.

## 5) Модификаторные обёртки keycode

Это не отдельные behaviors, а функции-обёртки keycode:

- `LS(X)` — Shift + `X`
- `LC(X)` — Ctrl + `X`
- `LA(X)` — Alt/Option + `X`
- `LG(X)` — GUI/Cmd + `X`
- `RA(X)` — Right Alt/AltGr + `X`

Можно вкладывать:

- `LS(RA(SLASH))` → Shift + RightAlt + Slash
- `LS(LC(LA(N1)))` → Shift + Ctrl + Alt + 1

## 6) Синтаксис devicetree, который тут постоянно встречается

- `bindings = <...>;` — список действий/аргументов.
- В `behavior-mod-morph` часто 2 биндинга:\
  `bindings = <tap_binding>, <shift_binding>;`
- `#binding-cells = <N>;` — сколько аргументов принимает behavior при вызове.
  - Пример: `#binding-cells = <2>` у hold-tap, поэтому вызов вида `&ht_curved LGUI BSPC`.

## 7) Комбо-макросы из `chords.dtsi`

Это C-preprocessor макросы, которые генерируют devicetree-ноды combo.

- `TCOMBO(...)` — полный комбо-набор (база + варианты с thumbs).
- `TCOMBO_NO_BASE(...)` — без базового одиночного комбо.
- `LAYER_TCOMBO(...)` — то же, но ограничено конкретным слоем.
- `LAYER_TCOMBO_NO_BASE(...)` — слой + без базового комбо.
- `COMBO_MIRROR_LAYERS(...)` — зеркальная пара комбо (левая/правая стороны).
- `COMBO_MIRROR_LAYERS_IDLE(...)` — зеркальная пара комбо с порогом «тишины» перед срабатыванием.
  - Что это значит: макрос создаёт левую и правую версии одного комбо, как `COMBO_MIRROR_LAYERS`, но добавляет `require-prior-idle-ms = <IDLE_MS>`.
  - На что влияет: комбо не сработает, если перед ним были недавние нажатия клавиш (меньше `IDLE_MS` мс назад). Это режет случайные срабатывания во время быстрой печати.
  - Как это ощущается:
    - `IDLE_MS` меньше (например 50) → комбо срабатывают легче/быстрее, но выше риск ложных срабатываний.
    - `IDLE_MS` больше (например 200) → комбо стабильнее, но нужно чуть заметнее «пауза перед аккордом».
  - Примеры из вашего `chords.dtsi`:
    - `COMBO_MIRROR_LAYERS_IDLE(lock_nav, ..., 150)` — `tog NAV_L` срабатывает только если перед аккордом было ~150 мс покоя.
    - `COMBO_MIRROR_LAYERS_IDLE(lock_mouse, ..., 150)` — то же для `tog MOUSE_L`.
  - Когда использовать: для «режимных» или опасных комбо (lock/toggle), где ложное срабатывание критичнее, чем небольшая задержка.

Параметры combo-нод, которые они генерируют:

- `timeout-ms` — окно одновременного нажатия для распознавания комбо.
- `key-positions` — позиции клавиш, формирующих комбо.
- `layers` — слои, на которых комбо активно.
- `require-prior-idle-ms` — защита от случайных срабатываний при потоке печати.

## 8) Позиционные alias (что такое `TLI`, `BLM`, `LIT`, `ROT`)

В `keymap` определены человекочитаемые alias на физические позиции:

- Левая сетка: `TLP TLR TLM TLI` (верх), `BLP BLR BLM BLI` (низ)
- Правая сетка: `TRP TRR TRM TRI` (верх), `BRP BRR BRM BRI` (низ)
- Большие пальцы:
  - `LIT`, `LOT` — левая рука (inner/outer thumb)
  - `RIT`, `ROT` — правая рука (inner/outer thumb)

Именно эти alias используются в `key-positions` комбо-макросов.

## 9) Быстрые примеры чтения строк

- `&lt HOLD_NUM_L B`\
  \= тап `B`, удержание временно включает слой `HOLD_NUM_L`.
- `&ht_curved LGUI BSPC`\
  \= поведение hold-tap: hold даёт `LGUI`, tap даёт `BSPC`.
- `TCOMBO(f, &kp F, &kp LS(F), &kp UP, &kp LS(UP), TLR, TRR)`\
  \= генерируются комбо для `f` на обеих половинах, включая варианты с thumb-модификаторами.

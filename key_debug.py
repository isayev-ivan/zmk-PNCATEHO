import sys

try:
    from pynput import keyboard
except ImportError:
    print("Ошибка: Библиотека 'pynput' не установлена.")
    print("Пожалуйста, установите её командой: pip3 install pynput")
    sys.exit(1)

def on_press(key):
    try:
        # Для буквенно-цифровых клавиш
        key_char = key.char
        vk = getattr(key, 'vk', 'N/A')
        print(f'Нажат cимвол: {key_char} | Key code: {vk}')
    except AttributeError:
        # Для специальных клавиш (Shift, Ctrl, и т.д.)
        key_name = str(key).replace('Key.', '')
        vk = getattr(key.value, 'vk', 'N/A') if hasattr(key, 'value') else 'N/A'
        print(f'Спец. клавиша: {key_name} | Key code: {vk}')

def on_release(key):
    if key == keyboard.Key.esc:
        # Остановить слушатель
        return False

print("=== Тест Клавиатуры ===")
print("Нажимайте клавиши, чтобы увидеть их коды.")
print("Для выхода нажмите ESC.")
print("ВНИМАНИЕ: На macOS может потребоваться разрешение 'Input Monitoring' для терминала.")
print("=======================")

# Запуск слушателя
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

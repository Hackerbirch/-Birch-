@echo off
:: Назва: BIRCH Launcher
:: Опис: запускає birch.exe з переданим файлом .birch

:: 1. Шлях до birch.exe (поклади birch.exe в ту ж папку)
set BIRCH_EXE=%~dp0birch.exe

:: 2. Перевірка: чи файл переданий
if "%~1"=="" (
    echo Перетягни .birch файл на цей бат або відкрий через нього
    pause
    exit
)

:: 3. Запуск birch.exe з файлом
"%BIRCH_EXE%" "%~1"

:: 4. Чекати, щоб побачити результат
pause
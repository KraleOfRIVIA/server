Проект: Система обработки данных от робототехнического устройства с использованием нейросети и технологий AR/VR
Описание проекта

Этот проект реализует систему для сбора, обработки и отображения информации от робототехнического устройства и сервера с нейросетью, используя технологии дополненной (AR) и виртуальной реальности (VR).

В проекте реализованы три компонента:

    Клиент (робот): Устройство, которое собирает данные (сенсоры, камеры и т.д.) и передает их на сервер для дальнейшей обработки.
    Сервер (нейросеть): Система обработки данных, в основе которой лежит нейронная сеть. Сервер принимает данные от робота, обрабатывает их и возвращает результат.
    Тестовый клиент (AR/VR): Приложение, которое принимает обработанный поток данных и визуализирует его с использованием AR/VR технологий.

Структура проекта

    client/: Директория с исходным кодом для клиента (робота). Этот компонент отвечает за сбор данных и отправку их на сервер.
    server/: Исходный код сервера, где происходит обработка данных нейросетью.
    test-client/: Тестовый клиент для визуализации данных с использованием AR/VR.

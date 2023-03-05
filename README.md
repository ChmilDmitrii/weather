#### Добавляем файлу `weather` права на выполнение
```bash
cd /weather-yt
chmod +x weather
```

#### Прокидываем симлинк (ярлык) на исполнимый файл `weather`
```bash
cd /weather-yt
sudo ln -s $(pwd)/weather /usr/local/bin/
```

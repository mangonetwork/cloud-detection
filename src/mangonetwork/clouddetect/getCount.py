import getUrls
greenCountClear = 0
greenCountCloudy = 0
redCountClear = 0
redCountCloudy = 0
for url in getUrls.getURL():
    urlSplice = url[0][-30:][:2]
    print(urlSplice)
    
    if (urlSplice.startswith('gr')):
        if url[1] == 'Y':
            greenCountClear += 1
        else:
            greenCountCloudy += 1
    else:
        if url[1] == 'Y':
            redCountClear += 1
        else:
            redCountCloudy += 1
print(f'Clear Reds: {redCountClear}')
print(f'Cloudy Reds: {redCountCloudy}')
print(f'Clear Greens: {greenCountClear}')
print(f'Cloudy Greens: {greenCountCloudy}')
print(f'Total Reds: {redCountClear + redCountCloudy}')
print(f'Total Greens: {greenCountClear + greenCountCloudy}')
print(f'Total Images: {greenCountClear + greenCountCloudy + redCountClear + redCountCloudy}')


names = ['一色','かわさき','かわさきしんじ','遠藤']
target = 'かわさき'
found = False

for name in names:
    if target in name:
        print(f'発見:{name}')
        found = True
        continue
    print('繰り返し処理を継続します。')
if not found:
    print('見つかりませんでした。')
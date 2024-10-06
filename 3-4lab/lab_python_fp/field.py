goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'color': 'black'}
]
def field(items, *args):
    assert len(args)>0
    for item in items:
        result={key: item.get(key) for key in args if item.get(key) is not None}
        if len(args)==1:
            yield result[args[0]]
        else:
            yield result

Nekto = list(field(goods,'title'))
print(', '.join(Nekto))
Nekto2 =list(field(goods,'title','price'))
print(', '.join(str(Nekto3) for Nekto3 in Nekto2))
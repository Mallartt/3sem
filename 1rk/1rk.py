from operator import itemgetter
class House:
    def __init__(self,id,number,cost,street_id):
        self.id=id
        self.number=number
        self.cost=cost
        self.street_id=street_id
class Street:
    def __init__(self,id,name):
        self.id=id
        self.name=name
class HouStr:
    def __init__(self,street_id,house_id):
        self.street_id=street_id
        self.house_id=house_id
streets=[
    Street(1,'Английский бульвар'),
    Street(2,'Амурская улица'),
    Street(3,'Абрикосовая улица'),
    Street(4,'Железнодорожная улица'),
    Street(5,'Приморская улица'),
    Street(6,'Острякова'),
]
houses=[
    House(1,111,9000,1),
    House(2,123,4500,2),
    House(3,125,3300,2),
    House(4,635,1200,3),
    House(5,325,6300,4),
    House(6,265,4400,4),
]
hou_str=[
    HouStr(1,1),
    HouStr(2,2),
    HouStr(2,3),
    HouStr(3,4),
    HouStr(4,5),
    HouStr(4,6),
    HouStr(5,1),
    HouStr(6,2),
]
def main():
    one_to_many=[(h.number,h.cost,s.name)
                 for h in houses
                 for s in streets
                 if  h.street_id==s.id]
    many_to_many_temp = [(s.name,hs.house_id,hs.street_id)
                         for s in streets
                         for hs in hou_str
                         if s.id==hs.street_id]
    many_to_many = [(h.number, h.cost, s.name)
                    for hs in hou_str
                    for h in houses if h.id == hs.house_id
                    for s in streets if s.id == hs.street_id]
    print('Задание Г1')
    res_1 = {}
    for s in streets:
        if s.name[0]=='А':
            h_s = [(house.number, house.cost) for house in houses if house.street_id == s.id]
            res_1[s.name] = h_s
    print(res_1)
    print ('Задание Г2')
    res_2=[]
    for s in streets:
        s_houses=list(filter(lambda i:i[2]==s.name,one_to_many))
        if len(s_houses)>0:
            s_costs=[cost for _,cost, _ in s_houses]
            s_max=max(s_costs)
            res_2.append((s.name,s_max))
    res_2=sorted(res_2,key=itemgetter(1),reverse=True)
    print(res_2)
    print('Задание Г3')
    res_3=sorted(many_to_many,key=itemgetter(2))
    print(res_3)

if __name__ =='__main__':
    main()
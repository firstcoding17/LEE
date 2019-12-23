import pandas as pd

Call_Data = pd.read_csv("DB.csv")
Menu_List = ["UserID", "WriteID",  "Favor_or_not"]
UserID = Call_Data[Menu_List[0]]
WriteList = Call_Data[Menu_List[1]]
Favor = Call_Data[Menu_List[2]]

"""
일단 한 유저가 뭘 봤는지 검색해야함
내부는 알아서 만들어 줄테니까
나가는거랑 들어오는거는 알아서 하센
"""
def Set_WriteList():
    Turn_Back_List = []
    for i in  range(0,len(Call_Data)):
        if WriteList[i] not in Turn_Back_List:
            Turn_Back_List.append(WriteList[i])
    return Turn_Back_List

def Set_USELRList():
    UserBackList=[]
    for i in range(0,len(Call_Data)):
        if UserID[i] not in UserBackList:
            UserBackList.append(UserID[i])
    return UserBackList

def check_How_Simmilar(integer, recommendation):
    turn_back_num = 0
    Recommendation_List = []
    Recommendation_List_T_or_F = []
    for i in range(0,len(Call_Data)):
        if UserID[i] == recommendation and WriteList[i] not in Recommendation_List and Favor[i] not in Recommendation_List_T_or_F:
            Recommendation_List.append(WriteList[i])
            Recommendation_List_T_or_F.append(Favor[i])
    Integer_List =[]
    Integer_List_T_or_F = []
    for i in range(0,len(Call_Data)):
        if UserID[i] == integer and WriteList[i] not in Integer_List and Favor[i] not in Integer_List_T_or_F:
            Integer_List.append(WriteList[i])
            Integer_List_T_or_F.append(Favor[i])
    for i in range(0,len(Recommendation_List)):
        if Recommendation_List[i] in Integer_List and Recommendation_List_T_or_F[i] == True:
            turn_back_num = turn_back_num+1
    return turn_back_num


def __main__():
    recommendation_User = 1 #임의로 설정한 값 추천을 해줘야하는 유저 대상
    List_about_WriteNum = Set_WriteList()
    List_about_USER = Set_USELRList() #순서인데 아마 똑같은거 하나 있을 듯
    SunWee = [] #각 리스트마다 점수
    for j in range(0,len(List_about_USER)):
        N = check_How_Simmilar(UserID[j],recommendation_User)

        SunWee.append(N)

























if __name__ == "__main__":
    __main__()
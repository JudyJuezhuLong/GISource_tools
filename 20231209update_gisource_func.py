# 基本模板
import datetime
from IPython.display import clear_output

# Edit contact information
def contactInfo(contact_people=[''],contact_email=['']):
    contac_info = ''
    for i in range(len(contact_people)):
        if contact_people[i]=='':
            contac_info = contac_info+contact_people[i]+contact_email[i]+', '
        else:
            contac_info = contac_info + 'Dr. '+contact_people[i]+' ('+contact_email[i]+'), '
    contac_info = contac_info[:-2]
    return contac_info
    pass

# Format UTC time
def getUtcDate():
    utc_time = datetime.datetime.utcnow()
    return utc_time.strftime('%Y-%m-%d %H:%M:%S')
    pass

# Replace the empty to 【】
def replaceEmpty(check_list):
    for i in range(len(check_list)):
        if check_list[i]=='':
            check_list[i] = check_list[i].replace('', '【】' )
    return check_list
    
# Generate the name of position
def typePosition(type_position = False,University_EN='',University_CN='',Country_EN='',Country_CN=''):
    if type_position == 0:
        Job_EN='Doctoral Student'
        Job_CN='博士研究生'

    elif type_position == 1:
        Job_EN='Master\'s Student'
        Job_CN='硕士研究生'

    elif type_position == 2:
        Job_EN='Doctoral student【and/or】 Master\'s student'
        Job_CN='博士研究生【和/或】硕士研究生'
        
    elif type_position == 3:
        Job_EN='PostDoc'
        Job_CN='博士后'
        
    else:
        Job_EN=''
        Job_CN=''

    Job_EN,Job_CN=replaceEmpty([Job_EN,Job_CN])
    Title_EN=University_EN+' in '+Country_EN+' is recruiting for a '+Job_EN
    if Country_CN == University_CN[:len(Country_CN)]:
        Country_CN=''
    Title_CN=Country_CN+University_CN+'招聘'+Job_CN
    return Job_EN,Job_CN,Title_EN,Title_CN

# Print the name of position
def typePositionName(type_position):
    if type_position == 0:
        type_position_name='PhD_position'
    elif type_position == 1:
        type_position_name='Masters_position'
    elif type_position == 2:
        type_position_name='PhD_Masters_position'
    elif type_position == 3:
        type_position_name='PostDoc'
    else:
        type_position_name=''
    return type_position_name

# Edit database information
def dataBase(type_position = False,University_CN='',University_EN='',Country_CN='',Country_EN='',\
             direction='',deadline='',URL='',contact_people=[''],contact_email=['']):
    utc_time = getUtcDate()
    my_str = 'UTC 时间：'+utc_time+'\n'
    
    Job_EN,Job_CN,Title_EN,Title_CN=typePosition(type_position,University_EN,University_CN,Country_EN,Country_CN)
    contact = contactInfo(contact_people,contact_email)
    University_CN,University_EN,Country_CN,Country_EN,direction,deadline,URL,Job_EN,Job_CN,Title_EN,Title_CN,contact=\
    replaceEmpty([University_CN,University_EN,Country_CN,Country_EN,direction,deadline,URL,Job_EN,Job_CN,Title_EN,Title_CN,contact])
    my_str = my_str + dataBase_SQL_insert(University_CN,University_EN,Country_CN,Country_EN,Job_EN,Job_CN,Title_EN,Title_CN)
    my_str = my_str + '\n\n<p>'+direction+r'; \nDeadline: '+deadline+r'; \nContact: '+contact+r'; \nURL: '+URL+'</p>'
    return my_str
    pass

# SQL insert one record
def dataBase_SQL_insert(University_CN='',University_EN='',Country_CN='',Country_EN='',Job_EN='',Job_CN='',Title_EN='',Title_CN=''):
    Date=getUtcDate()[:10]
    my_str = '\nUSE TEST;'
    my_str = my_str + '\nINSERT INTO TEST.GISource (University_CN,University_EN,Country_CN,Country_EN,Job_CN,Job_EN,Title_CN,Title_EN,Date)'
    if '\'' in Job_EN:
        Job_EN = Job_EN.replace('\'', '\\\'' )
        Title_EN = Title_EN.replace('\'', '\\\'' )
        my_str=my_str + '\nVALUES (\''+University_CN+'\', \''+University_EN+'\', \''+Country_CN+'\',\''+Country_EN+'\',\''+Job_CN+'\',\''+Job_EN+'\',\''+Title_CN+'\',\''+Title_EN+'\',\''+Date+'\');'
    else:
        my_str=my_str + '\nVALUES (\''+University_CN+'\', \''+University_EN+'\', \''+Country_CN+'\',\''+Country_EN+'\',\''+Job_CN+'\',\''+Job_EN+'\',\''+Title_CN+'\',\''+Title_EN+'\',\''+Date+'\');'

    return my_str
    pass

# Edit WeChat information
def weChat(type_position=False,Country_CN='',University_CN='',direction='',deadline='',\
           contact_people=[''],contact_email=[''],URL=''):
    weChat_label=''
    contact = contactInfo(contact_people,contact_email)
    University_CN,Country_CN,direction,deadline,URL,contact,weChat_label=\
    replaceEmpty([University_CN,Country_CN,direction,deadline,URL,contact,weChat_label])
    deadline_ls=deadline.split('-')
    this_year=getUtcDate()[:4]
    my_str = ''
    Country_CN_=Country_CN
    if Country_CN == University_CN[:len(Country_CN)]:
        Country_CN_=''
    if type_position == 0:
        my_str = Country_CN_+University_CN+' '+direction+' 方向 PhD 机会\n\n'
        weChat_label='标签：'+Country_CN+'；博士机会；【???】'
    elif type_position == 1:
        my_str = Country_CN_+University_CN+' '+direction+' 方向硕士机会\n\n'
        weChat_label='标签：'+Country_CN+'；硕士机会；【???】'
    elif type_position == 2:
        my_str = Country_CN_+University_CN+' '+direction+' 方向硕士【和/或】博士机会\n\n'
        weChat_label='标签：'+Country_CN+'；博士机会；硕士机会；【???】'
    elif type_position == 3:
        my_str = Country_CN_+University_CN+' '+direction+' 方向 PostDoc 机会\n\n'
        weChat_label='标签：'+Country_CN+'；博后机会；【???】'
    else:
        #my_str = '不是招聘信息'+'\n'
        #weChat_label='标签：'+Country_CN+'；【???】'
        my_str = Country_CN+University_CN+' '+direction+' 方向【position_name】机会\n\n'
        weChat_label='标签：'+Country_CN+'；【position_name】机会；【???】'
    
    if len(deadline_ls)==3:
        if this_year==deadline_ls[0]:
            my_str = my_str +str(int(deadline_ls[1]))+'月'+str(int(deadline_ls[2]))+'日'+'截止申请, '
        else:
            my_str = my_str +deadline_ls[0]+'年'+str(int(deadline_ls[1]))+'月'+str(int(deadline_ls[2]))+'日'+'截止申请, '
    else:
        my_str = my_str + '尽快申请, '
        
    my_str = my_str + '有意者请联系 '+contact+'\n\n'
#     my_str = my_str + '详情见'+URL+'\n\n'
    my_str = my_str + '链接:【GISphere链接】\n\n'
    my_str = my_str + weChat_label
    
    return my_str
    pass

# Edit WhatsApp information
def whatsApp(type_position=False,Country_EN='',University_EN='',direction='',deadline='',\
           contact_people=[''],contact_email=[''],URL=''):
    whatsApp_label=''
    contact = contactInfo(contact_people,contact_email)
    University_EN,Country_EN,direction,deadline,URL,contact,whatsApp_label=\
    replaceEmpty([University_EN,Country_EN,direction,deadline,URL,contact,whatsApp_label])
    
    my_str = 'Direction: '+direction+'\n\n'
    if type_position == 0:
        my_str = my_str + 'Tags: '+'PhD opportunity in '+University_EN+'\n\n'
        whatsApp_label=Country_EN+'; PhD opportunity;【???】'
    elif type_position == 1:
        my_str = my_str + "Master's opportunity in "+University_EN+'\n\n'
        whatsApp_label='Tags: '+Country_EN+"; Master's opportunity;【???】"
    elif type_position == 2:
        my_str = my_str + "PhD 【and/or】 Master's opportunity in "+University_EN+'\n\n'
        whatsApp_label='Tags: '+Country_EN+"; PhD 【and/or】 Master's opportunity;【???】"
    elif type_position == 3:
        my_str = my_str + 'PostDoc opportunity in '+University_EN+'\n\n'
        whatsApp_label='Tags: '+Country_EN+'; PostDoc opportunity;【???】'
    else:
        my_str = my_str + '【position_name】 opportunity in '+University_EN+'\n\n'
        whatsApp_label='Tags: '+Country_EN+'; 【position_name】 opportunity;【???】'
    my_str = my_str + 'Deadline：'+deadline+'\n\n'
    my_str = my_str + 'Contact：'+contact+'\n\n'
#     my_str = my_str + 'URL：'+URL+'\n\n'
    my_str = my_str + 'URL：【GISphere链接】\n\n'
    my_str = my_str + whatsApp_label

    return my_str
    pass

def outputStr(type_position_name,database_info,wechat_info,whatsapp_info):
    my_str = ' **** '+type_position_name+' 基本模板 ****'
    my_str = my_str + '\n\n---------------- 数据库 -------------------\n'
    my_str = my_str + database_info
    my_str = my_str + '\n\n--------------- 微信聊天群 ------------------\n'
    my_str = my_str + wechat_info
    my_str = my_str + '\n\n--------------- WhatsApp聊天群 ------------------\n'
    my_str = my_str + whatsapp_info
    return my_str

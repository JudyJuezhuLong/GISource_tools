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
    str = 'UTC 时间：'+utc_time+'\n'
    
    Job_EN,Job_CN,Title_EN,Title_CN=typePosition(type_position,University_EN,University_CN,Country_EN,Country_CN)
    contact = contactInfo(contact_people,contact_email)
    University_CN,University_EN,Country_CN,Country_EN,direction,deadline,URL,Job_EN,Job_CN,Title_EN,Title_CN,contact=\
    replaceEmpty([University_CN,University_EN,Country_CN,Country_EN,direction,deadline,URL,Job_EN,Job_CN,Title_EN,Title_CN,contact])
    str = str + dataBase_SQL_insert(University_CN,University_EN,Country_CN,Country_EN,Job_EN,Job_CN,Title_EN,Title_CN)
    str = str + '\n\n<p>'+direction+r'; \nDeadline: '+deadline+r'; \nContact: '+contact+r'; \nURL: '+URL+'</p>'
    return str
    pass

# SQL insert one record
def dataBase_SQL_insert(University_CN='',University_EN='',Country_CN='',Country_EN='',Job_EN='',Job_CN='',Title_EN='',Title_CN=''):
    Date=getUtcDate()[:10]
    str = '\nUSE TEST;'
    str = str + '\nINSERT INTO GISource (University_CN,University_EN,Country_CN,Country_EN,Job_CN,Job_EN,Title_CN,Title_EN,Date)'
    if '\'' in Job_EN:
        Job_EN = Job_EN.replace('\'', '\\\'' )
        Title_EN = Title_EN.replace('\'', '\\\'' )
        str=str + '\nVALUES (\''+University_CN+'\', \''+University_EN+'\', \''+Country_CN+'\',\''+Country_EN+'\',\''+Job_CN+'\',\''+Job_EN+'\',\''+Title_CN+'\',\''+Title_EN+'\',\''+Date+'\');'
    else:
        str=str + '\nVALUES (\''+University_CN+'\', \''+University_EN+'\', \''+Country_CN+'\',\''+Country_EN+'\',\''+Job_CN+'\',\''+Job_EN+'\',\''+Title_CN+'\',\''+Title_EN+'\',\''+Date+'\');'

    return str
    pass

# Edit WeChat information
def weChat(type_position=False,Country_CN='',University_CN='',direction='',deadline='',\
           contact_people=[''],contact_email=[''],URL=''):
    weChat_label=''
    contact = contactInfo(contact_people,contact_email)
    University_CN,Country_CN,direction,deadline,URL,contact,weChat_label=\
    replaceEmpty([University_CN,Country_CN,direction,deadline,URL,contact,weChat_label])
    deadline_ls=deadline.split('-')
        
    str = ''
    if type_position == 0:
        str = Country_CN+University_CN+' '+direction+' 方向 PhD 机会\n\n'
        weChat_label='标签：'+Country_CN+'；博士机会；【???】'
    elif type_position == 1:
        str = Country_CN+University_CN+' '+direction+' 方向硕士机会\n\n'
        weChat_label='标签：'+Country_CN+'；硕士机会；【???】'
    elif type_position == 2:
        str = Country_CN+University_CN+' '+direction+' 方向硕士【和/或】博士机会\n\n'
        weChat_label='标签：'+Country_CN+'；博士机会；硕士机会；【???】'
    elif type_position == 3:
        str = Country_CN+University_CN+' '+direction+' 方向 PostDoc 机会\n\n'
        weChat_label='标签：'+Country_CN+'；博后机会；【???】'
    else:
        #str = '不是招聘信息'+'\n'
        #weChat_label='标签：'+Country_CN+'；【???】'
        str = Country_CN+University_CN+' '+direction+' 方向【position_name】机会\n\n'
        weChat_label='标签：'+Country_CN+'；【position_name】机会；【???】'
    
    if len(deadline_ls)==3:
        str = str +deadline_ls[0]+'年'+deadline_ls[1]+'月'+deadline_ls[2]+'日'+'截止申请, '
    else:
        str = str + '尽快申请, '
        
    str = str + '有意者请联系 '+contact+'\n\n'
#     str = str + '详情见'+URL+'\n\n'
    str = str + '链接:【GISphere链接】\n\n'
    str = str + weChat_label
    
    return str
    pass

# Edit WhatsApp information
def whatsApp(type_position=False,Country_EN='',University_EN='',direction='',deadline='',\
           contact_people=[''],contact_email=[''],URL=''):
    whatsApp_label=''
    contact = contactInfo(contact_people,contact_email)
    University_EN,Country_EN,direction,deadline,URL,contact,whatsApp_label=\
    replaceEmpty([University_EN,Country_EN,direction,deadline,URL,contact,whatsApp_label])
    
    str = 'Direction: '+direction+'\n\n'
    if type_position == 0:
        str = str + 'Tags: '+'PhD opportunity in '+University_EN+'\n\n'
        whatsApp_label=Country_EN+'; PhD opportunity;【???】'
    elif type_position == 1:
        str = str + "Master's opportunity in "+University_EN+'\n\n'
        whatsApp_label='Tags: '+Country_EN+"; Master's opportunity;【???】"
    elif type_position == 2:
        str = str + "PhD 【and/or】 Master's opportunity in "+University_EN+'\n\n'
        whatsApp_label='Tags: '+Country_EN+"; PhD 【and/or】 Master's opportunity;【???】"
    elif type_position == 3:
        str = str + 'PostDoc opportunity in '+University_EN+'\n\n'
        whatsApp_label='Tags: '+Country_EN+'; PostDoc opportunity;【???】'
    else:
        str = str + '【position_name】 opportunity in '+University_EN+'\n\n'
        whatsApp_label='Tags: '+Country_EN+'; 【position_name】 opportunity;【???】'
    str = str + 'Deadline：'+deadline+'\n\n'
    str = str + 'Contact：'+contact+'\n\n'
#     str = str + 'URL：'+URL+'\n\n'
    str = str + 'URL：【GISphere链接】\n\n'
    str = str + whatsApp_label

    return str
    pass

def outputStr(type_position_name,database_info,wechat_info,whatsapp_info):
    str = ' **** '+type_position_name+' 基本模板 ****'
    str = str + '\n\n---------------- 数据库 -------------------\n'
    str = str + database_info
    str = str + '\n\n--------------- 微信聊天群 ------------------\n'
    str = str + wechat_info
    str = str + '\n\n--------------- WhatsApp聊天群 ------------------\n'
    str = str + whatsapp_info
    return str
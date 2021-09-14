file_handle = open('long_text.txt')
content0 = file_handle.readlines()
content = content0[1:-1]
for line in range(len(content)):
    content[line] = content[line].strip('\n')
final_dict = {}
final_dict['name'] = content[0]
final_dict['lei'] = content[1]
sub_fund_value=[]
flag1 = 0
for i in range(2,len(content)):
    if '.' in content[i]:
        flag1 = flag1 + 1
        title_str = content[i].replace(str(flag1)+'. ','')
        sub_fund_value.append({'title':title_str})
        isin_list=[]
    else:
        isin_list.append(content[i])
        sub_fund_value[flag1-1]['isin'] = isin_list

final_dict['sub_fund'] = sub_fund_value

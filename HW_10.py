#"""
#�� ����� ����� n �������. ��������� �� ��� ����� ����� ������, � ��������� � ������. 
#���������� ����������� ����� �������, ������� ����� �����������, 
#����� ��� ������� ���� ��������� ����� ����� � ��� �� ��������. 
#�������� ����������� ���������� �����, ������� ����� �����������
#"""

from random import randint
n = randint(1,10)
counterzero=0
counterfirst=0
for i in range(1,n+1):
    i = randint(0,1)
    print(i)
    if i==0:
        counterzero+=1
    else:
        counterfirst+=1
if counterzero<counterfirst:
    print(f"���������� ���������� �����, ������� ����� ����������� =  {counterzero}")
else:
    print(f"���������� ���������� �����, ������� ����� ����������� =  {counterfirst}")















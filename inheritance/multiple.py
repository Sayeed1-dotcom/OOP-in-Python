class A:
    f_name = "Mohammad Absar"

class B:
    m_name = "Zinnat Begum"

   #multiple inheritance
class C(A,B):
    name = "Afrin Absar"

s1 = C()
print(s1.name)
print(s1.f_name)
print(s1.m_name)

def Bohr_to_Ang(ang):
    bohr= ang * ((0.529177249)**3)*(10**(-24)) 
    return bohr

def format_e(n):
    a = '%E' % n
    print a
    return a.split('E')[0].rstrip('0').rstrip('.') + 'E' + a.split('E')[1]

volume_b=Bohr_to_Ang(452.85341)
N=0.671059513625535
y = N/volume_b
# print y
h = '%E' % y
print h

new =format(y, '3g')
print float(new)

print "%. 0.1g" % y
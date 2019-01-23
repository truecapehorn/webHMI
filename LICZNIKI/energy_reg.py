from registers import regList


print('Lista rejestrów : {}'.format(len(regList)))

I1sum = []
I2sum = []
I3sum = []
U1avg =[]
U2avg = []
U3avg = []
P1sum = []
P2sum = []
P3sum = []
S1sum = []
S2sum = []
S3sum = []
Q1sum = []
Q2sum = []
Q3sum = []
Ep = []
Eq = []
for k, v in sorted(regList.items()):
    if '0 RG' in v['category']:

        if 'LE03' in v['plcname'] and v['plcname'] != 'LE03_SUM':
            print(k, v)
            if 'Natezenie pradu L1' in v['regtitle']:
                I1sum.append(k)
                I1sum =[int(i) for i in I1sum]
            if 'Natezenie pradu L2' in v['regtitle']:
                # print(k, v)
                I2sum.append(k)
                I2sum = [int(i) for i in I2sum]
            if 'Natezenie pradu L3' in v['regtitle']:
                I3sum.append(k)
                I3sum = [int(i) for i in I3sum]


            if 'Napiecie fazowe L1 (L-N)' in v['regtitle']:
                # print(k, v)
                U1avg.append(k)
                U1avg =[int(i) for i in U1avg]
            if 'Napiecie fazowe L2 (L-N)' in v['regtitle']:
                # print(k, v)
                U2avg.append(k)
                U2avg = [int(i) for i in U2avg]
            if 'Napiecie fazowe L3 (L-N)' in v['regtitle']:
                U3avg.append(k)
                U3avg= [int(i) for i in U3avg]



            if 'Moc czynna L1' in v['regtitle']:
                # print(k, v)
                P1sum.append(k)
                P1sum = [int(i) for i in P1sum]
            if 'Moc czynna L2' in v['regtitle']:
                # print(k, v)
                P2sum.append(k)
                P2sum = [int(i) for i in P2sum]
            if 'Moc czynna L3' in v['regtitle']:
                P3sum.append(k)
                P3sum = [int(i) for i in P3sum]

            if 'Moc pozorna L1' in v['regtitle']:
                # print(k, v)
                S1sum.append(k)
                S1sum = [int(i) for i in S1sum]
            if 'Moc pozorna L2' in v['regtitle']:
                # print(k, v)
                S2sum.append(k)
                S2sum = [int(i) for i in S2sum]
            if 'Moc pozorna L3' in v['regtitle']:
                S3sum.append(k)
                S3sum = [int(i) for i in S3sum]

            if 'Moc bierna L1' in v['regtitle']:
                # print(k, v)
                Q1sum.append(k)
                Q1sum = [int(i) for i in Q1sum]
            if 'Moc bierna L2' in v['regtitle']:
                # print(k, v)
                Q2sum.append(k)
                Q2sum = [int(i) for i in Q2sum]
            if 'Moc bierna L3' in v['regtitle']:
                Q3sum.append(k)
                Q3sum = [int(i) for i in Q3sum]


            if 'Calkowita energia czynna' in v['regtitle']:
                # print(k, v)
                Ep.append(k)
                Ep = [int(i) for i in Ep]
            if 'Calkowita energia bierna' in v['regtitle']:
                # print(k, v)
                Eq.append(k)
                Eq = [int(i) for i in Eq]


        if 'LE01' in v['plcname']:
            print(k ,v)
            if 'Prad' in v['regtitle']:
                # print(k, v)
                I1sum.append(k)
                I1sum = [int(i) for i in I1sum]


            if 'Napiecie' in v['regtitle']:
                # print(k, v)
                U1avg.append(k)
                U1avg = [int(i) for i in U1avg]


            if 'Moc czynna' in v['regtitle']:
                # print(k, v)
                P1sum.append(k)
                P1sum = [int(i) for i in P1sum]


            if 'Moc pozorna' in v['regtitle']:
                # print(k, v)
                S1sum.append(k)
                S1sum = [int(i) for i in S1sum]


            if 'Moc bierna' in v['regtitle']:
                # print(k, v)
                Q1sum.append(k)
                Q1sum = [int(i) for i in Q1sum]


            if 'Cal. energia czynna' in v['regtitle']:
                print(k, v)
                Ep.append(k)
                Ep = [int(i) for i in Ep]
            if 'Cal. energia bierna' in v['regtitle']:
                print(k, v)
                Eq.append(k)
                Eq = [int(i) for i in Eq]


print('--PRAD')
print('local I1_l =' ,I1sum)
print('local I2_l =' ,I2sum)
print('local I3_l =' ,I3sum)

print('--NAPIECIE')
print('local U1_l =' ,U1avg)
print('local U2_l =' ,U2avg)
print('local U3_l =' ,U3avg)

print('--MOC CZYNNA')
print('local P1sum_l =' ,P1sum)
print('local P2sum_l =' ,P2sum)
print('local P3sum_l =' ,P3sum)

print('--MOC POZORNA')
print('local S1sum_l =' ,S1sum)
print('local S2sum_l =' ,S2sum)
print('local S3sum_l =' ,S3sum)

print('--MOC BIERNA')
print('local Q1sum_l =' ,Q1sum)
print('local Q2sum_l =' ,Q2sum)
print('local Q3sum_l =' ,Q3sum)


print('--Energia czynna')
print('local Ep_l =' ,Ep)

print('--Energia bierna')
print('local Eq_l =' ,Eq)

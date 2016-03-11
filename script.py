import string
import operator

arifmetics = ['add', 'addi', 'addiu', 'addu', 'clo', 'clz', 'dadd', 'daddi',
'daddiu', 'daddu', 'dclo', 'dclz', 'ddiv', 'ddivu', 'div', 'divu', 'dmult',
'dmultu', 'dsub', 'dsubu', 'madd','maddu', 'msub', 'msubu', 'mul', 'mult',
'multu', 'slt', 'slti', 'sltiu', 'sltu', 'sub', 'subu']

branch = ['b', 'bal', 'beq', 'bgez', 'bgezal', 'bgtz','bgtzl', 'blez', 'bltz', 'bltzal', 'bne', 'j', 'jal',
'jalr', 'jr', 'beql', 'bgezall', 'bgezl', 'blezl', 'bltzall', 'bltzl', 'bnel', 'bc1f', 'bc1fl', 'bc1t', 'bc1tl']

load_store = ['lb', 'lbu', 'ld', 'ldl', 'ldr', 'lh',
'lhu', 'll', 'lld', 'lw', 'lwl', 'lwr', 'lwu', 'pref', 'sb', 'sc', 'scd', 'sd','sw', 'sdl', 'sdr', 'sh', 'swl', 'swr', 'sync', 'ldc1',
'ldxc1', 'lwc1', 'lwxc1', 'prefx', 'sdc1', 'sdxc1', 'swc1', 'swxc1']

logic = ['and', 'andi', 'lui', 'nor', 'or', 'ori', 'xor', 'xori', 'dsll', 'dsll32',
'dsllv', 'dsra', 'dsra32', 'dsrav', 'dsrl', 'dsrl', 'dsrl32', 'dsrlv', 'sll', 'sllv', 'sra', 'srav', 'srl', 'srlv']

move = ['mfhi', 'mflo', 'movf', 'movn', 'movt', 'movz', 'mthi', 'mtlo']

floating = [
'abs.S', 'add.S', 'div.S', 'madd.S', 'msub.S', 'mul.S', 'neg.S', 'nmadd.S', 'recip.S',
'rsqrt.S', 'sqrt.S', 'sub.S', 'ceil.W.S', 'ceil.L.S', 'floor.S', 'round.S', 'trunc.S',
'cfc1,' 'ctc1', 'dmfc1', 'dmtc1', 'mtc1', 'mfc1', 'mov.S', 'movf.S',
'movn.S', 'movt.S', 'movz.S',

'abs.D', 'add.D', 'div.D', 'madd.D', 'msub.D', 'mul.D', 'neg.D', 'nmadd.D', 'recip.D',
'rsqrt.D', 'sqrt.D', 'sub.D', 'ceil.W.D', 'ceil.L.D', 'cvt.D', 'floor.D', 'round.D', 'trunc.D',
'mov.D', 'movf.D','movn.D', 'movt.D', 'movz.D',

'abs.ps', 'add.ps', 'div.ps', 'madd.ps', 'msub.ps', 'mul.ps', 'neg.ps', 'nmadd.ps', 'recip.ps',
'rsqrt.ps', 'sqrt.ps', 'sub.ps', 'ceil.ps', 'cvt.ps', 'floor.ps', 'round.ps', 'trunc.ps',
'mov.ps', 'movf.ps', 'movn.ps', 'movt.ps', 'movz.ps',

'c.F.S', 'c.UN.S', 'c.EQ.S', 'c.UEQ.S', 'c.OLT.S', 'c.ULT.S', 'c.OLE.S', 'c.ULE.S', 'c.SF.S',
'c.NGLE.S', 'c.SEQ.S', 'c.NGL.S', 'c.LT.S', 'c.NGE.S', 'c.LE.S', 'c.NGT.S',
'c.F.D', 'c.UN.D', 'c.EQ.D', 'c.UEQ.D', 'c.OLT.D', 'c.ULT.D', 'c.OLE.D', 'c.ULE.D', 'c.SF.D',
'c.NGLE.D', 'c.SEQ.D', 'c.NGL.D', 'c.LT.D', 'c.NGE.D', 'c.LE.D', 'c.NGT.D',
'c.F.ps', 'c.UN.ps', 'c.EQ.ps', 'c.UEQ.ps', 'c.OLT.ps', 'c.ULT.ps', 'c.OLE.ps', 'c.ULE.ps', 'c.SF.ps',
'c.NGLE.ps', 'c.SEQ.ps', 'c.NGL.ps', 'c.LT.ps', 'c.NGE.ps', 'c.LE.ps', 'c.NGT.ps',
'cvt.D.S', 'cvt.D.W','cvt.D.L', 'cvt.L.S','cvt.L.D','cvt.ps.S', 'cvt.S.D', 'cvt.S.W','cvt.S.L', 'cvt.S.PL', 'cvt.S.PU',
'cvt.W.S', 'cvt.W.D']

nop = ['nop', 'ssnop', 'ehb']

privileged = ['cache', 'cfc0', 'ctc0', 'dmfc0', 'dmtc0', 'eret', 'mfc0',
'mtc0', 'tlbp', 'tlbr', 'tlbwi', 'tlbwr','wait']


def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in xrange(0, len(l), n):
        yield l[i:i+n]

def instruction_annotation(x):
    if x in arifmetics:
        return 'A'
    elif x in branch:
        return 'B'
    elif x in load_store:
        return 'S'
    elif x in logic:
        return 'L'
    elif x in move:
        return 'M'
    elif x in floating:
        return 'F'
    elif x in nop:
        return 'N'
    elif x in privileged:
        return 'P'
    elif x in trap:
        return 'T'
    elif x == 'E':
        return x
    else :
        return '0'

        
def get_values(lVals):
    res = []
    for val in lVals:
        if type(val) not in [list, set, tuple]:
            res.append(val)
        else:
            res.extend(get_values(val))
    return res

f = open("log2.txt", "r").read().split('\n')

data = [",".join(f[i].split()) for i in range(len(f))]
data = [data[i].split(',') for i in range(len(f))]

databkp = data

print len(data)
#DELETE HEADER
for x in data:
    if 'START' not in x:
        del x
if not data:
    #VERY BAD FOR PERFORMANCE
    #DELETE THIS FUNCTIONALITY FIRST IF APP IS TOO SLOW
    data = data1

exceptions = [i+1 for i in range(0, len(data)) if 'Exception' in data[i]]
eret       = [i for i in range(0, len(data)) if 'eret' in data[i]]
mask       = [range(i,j+1) for (i,j) in list(zip(exceptions, eret))]
mask = list(set(range(1,len(data))) - set(get_values(mask)))

#print mask
# DELETE EXCEPTION INSTRUCTIONS
data = [data[i] for i in mask]




for i in range(0, len(data)) :
    if 'Exception' in data[i]:
        data[i][4] = 'E'

# CHECK FOR BUG
#print len(data)
#for i in range(0, len(data)-1):
#    if data[i][0].isdigit():
#        if instruction_annotation(data[i][4]) == '0':
#            print data[i]


data_prepared = [data[i][4] for i in range(0,len(data)-1) if data[i][0].isdigit()]
data_prepared = list(chunks([instruction_annotation(i) for i in data_prepared], 4))[:-1]
data_prepared = ["".join(i) for i in data_prepared]
data_prepared = dict((x,data_prepared.count(x)) for x in set(data_prepared))
#print data_prepared

data_prepared = dict((key,val) for key,val in data_prepared.iteritems() if 'E' not in key or key[:-1] == 'E')
data_prepared = sorted(data_prepared.items(), key=operator.itemgetter(1), reverse=True)

f = open('tab.txt', 'w')
for index in data_prepared:
   f.write(str(index) + '\n')
f.close()
#print data_prepared




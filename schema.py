# coding=utf-8
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

#!/usr/bin/python

def devrunscemachange(schema):
    #print schema
    data=schema.split(",")
    osadmin = 'editfile  '+ '\"T1_OS_ADMIN_D\"' +"  "+ '\"' +data[0]+'\"'
    osruntime= 'editfile  '+ '\"T1_OS_RUNTIME_D\"' +"  "+ '\"' +data[1]+'\"'
    oslog = 'editfile  '+ '\"T1_OS_LOG_D\"' +"  "+ '\"' +data[2]+'\"'
    osstate = 'editfile  ' + '\"T1_OS_STATE_D\"' + "  " + '\"' + data[3] + '\"'
    schema=" "+osadmin+"\n"+" "+osruntime+"\n"+" "+oslog+"\n"+" "+osstate+"\n"
    with  open("./fast/env/server.hsconf.designfc", 'r') as schema_file:
        schemadata=schema_file.read()
        schemadata=schemadata.replace("T1_OS_ADMIN_D",data[0])
        schemadata = schemadata.replace("T1_OS_RUNTIME_D", data[1])
        schemadata = schemadata.replace("T1_OS_LOG_D", data[2])
        schemadata = schemadata.replace("T1_OS_STATE_D", data[3])
    with open("./fast/env/server.hsconf.designfc", 'w') as schema_file:
        schema_file.write(schemadata)
    with  open("./fast/bin/runawsschema.sh", 'r') as new_file:
        check="OS_STATE_PASSWD"
        value=""
        data=""
        finalfile=""
        filedata=new_file.read()
        for line in (filedata.split("\n")):
            if check in line:
                data=line
                print data
                value= data+"\n"+schema
                print value
        if schema not  in filedata:
            finalfile=filedata.replace(data,value)
            with  open("./fast/bin/runawsschema.sh", 'w') as new_file:
                new_file.write(finalfile)

def stgrunscemachange(schema):
    #print schema
    data=schema.split(",")
    osadmin = 'editfile  '+ '\"T1_OS_ADMIN_S\"' +"  "+ '\"' +data[0]+'\"'
    osruntime= 'editfile  '+ '\"T1_OS_RUNTIME_S\"' +"  "+ '\"' +data[1]+'\"'
    oslog = 'editfile  '+ '\"T1_OS_LOG_S\"' +"  "+ '\"' +data[2]+'\"'
    osstate = 'editfile  ' + '\"T1_OS_STATE_S\"' + "  " + '\"' + data[3] + '\"'
    schema=" "+osadmin+"\n"+" "+osruntime+"\n"+" "+oslog+"\n"+" "+osstate+"\n"
    with  open("./fast/env/server.hsconf.stagefc", 'r') as schema_file:
        schemadata=schema_file.read()
        schemadata=schemadata.replace("T1_OS_ADMIN_S",data[0])
        schemadata = schemadata.replace("T1_OS_RUNTIME_S", data[1])
        schemadata = schemadata.replace("T1_OS_LOG_S", data[2])
        schemadata = schemadata.replace("T1_OS_STATE_S", data[3])
    with open("./fast/env/server.hsconf.stagefc", 'w') as schema_file:
        schema_file.write(schemadata)
    with  open("./fast/env/server.hsconf.stagefe", 'r') as schema_file:
        schemadata=schema_file.read()
        schemadata=schemadata.replace("T1_OS_ADMIN_S",data[0])
        schemadata = schemadata.replace("T1_OS_RUNTIME_S", data[1])
        schemadata = schemadata.replace("T1_OS_LOG_S", data[2])
        schemadata = schemadata.replace("T1_OS_STATE_S", data[3])
    with open("./fast/env/server.hsconf.stagefe", 'w') as schema_file:
        schema_file.write(schemadata)
    with  open("./fast/bin/runawsschema.sh", 'r') as new_file:
        check="OS_STATE_PASSWD"
        value=""
        data=""
        finalfile=""
        filedata=new_file.read()
        for line in (filedata.split("\n")):
            if check in line:
                data=line
                print data
                value= data+"\n"+schema
                print value
        if value not  in filedata:
            finalfile=filedata.replace(data,value)
            with  open("./fast/bin/runawsschema.sh", 'w') as new_file:
                new_file.write(finalfile)
def prodrunscemachange(schema):
    #print schema
    data=schema.split(",")
    osadmin = 'editfile  '+ '\"T1_OS_ADMIN_O\"' +"  "+ '\"' +data[0]+'\"'
    osruntime= 'editfile  '+ '\"T1_OS_RUNTIME_O\"' +"  "+ '\"' +data[1]+'\"'
    oslog = 'editfile  '+ '\"T1_OS_LOG_O\"' +"  "+ '\"' +data[2]+'\"'
    osstate = 'editfile  ' + '\"T1_OS_STATE_O\"' + "  " + '\"' + data[3] + '\"'
    schema=" "+osadmin+"\n"+" "+osruntime+"\n"+" "+oslog+"\n"+" "+osstate+"\n"
    with  open("./fast/env/server.hsconf.prodfc", 'r') as schema_file:
        schemadata=schema_file.read()
        schemadata=schemadata.replace("T1_OS_ADMIN_O",data[0])
        schemadata = schemadata.replace("T1_OS_RUNTIME_O", data[1])
        schemadata = schemadata.replace("T1_OS_LOG_O", data[2])
        schemadata = schemadata.replace("T1_OS_STATE_O", data[3])
    with open("./fast/env/server.hsconf.prodfc", 'w') as schema_file:
        schema_file.write(schemadata)
    with  open("./fast/env/server.hsconf.prodfe", 'r') as schema_file:
        schemadata=schema_file.read()
        schemadata=schemadata.replace("T1_OS_ADMIN_O",data[0])
        schemadata = schemadata.replace("T1_OS_RUNTIME_O", data[1])
        schemadata = schemadata.replace("T1_OS_LOG_O", data[2])
        schemadata = schemadata.replace("T1_OS_STATE_O", data[3])
    with open("./fast/env/server.hsconf.prodfe", 'w') as schema_file:
        schema_file.write(schemadata)
    with  open("./fast/bin/runawsschema.sh", 'r') as new_file:
        check="OS_STATE_PASSWD"
        value=""
        data=""
        finalfile=""
        filedata=new_file.read()
        for line in (filedata.split("\n")):
            if check in line:
                data=line
                print data
                value= data+"\n"+schema
                print value
        if value not  in filedata:
            finalfile=filedata.replace(data,value)
            with  open("./fast/bin/runawsschema.sh", 'w') as new_file:
                new_file.write(finalfile)


def preprodrunscemachange(schema):
    # print schema
    data = schema.split(",")
    osadmin = 'editfile  ' + '\"T1_OS_ADMIN_O\"' + "  " + '\"' + data[0] + '\"'
    osruntime = 'editfile  ' + '\"T1_OS_RUNTIME_O\"' + "  " + '\"' + data[1] + '\"'
    oslog = 'editfile  ' + '\"T1_OS_LOG_O\"' + "  " + '\"' + data[2] + '\"'
    osstate = 'editfile  ' + '\"T1_OS_STATE_O\"' + "  " + '\"' + data[3] + '\"'
    schema = " " + osadmin + "\n" + " " + osruntime + "\n" + " " + oslog + "\n" + " " + osstate + "\n"
    with  open("./fast/env/server.hsconf.preprodfc", 'r') as schema_file:
        schemadata = schema_file.read()
        schemadata = schemadata.replace("T1_OS_ADMIN_O", data[0])
        schemadata = schemadata.replace("T1_OS_RUNTIME_O", data[1])
        schemadata = schemadata.replace("T1_OS_LOG_O", data[2])
        schemadata = schemadata.replace("T1_OS_STATE_O", data[3])
    with open("./fast/env/server.hsconf.preprodfc", 'w') as schema_file:
        schema_file.write(schemadata)
    with  open("./fast/env/server.hsconf.preprodfe", 'r') as schema_file:
        schemadata = schema_file.read()
        schemadata = schemadata.replace("T1_OS_ADMIN_O", data[0])
        schemadata = schemadata.replace("T1_OS_RUNTIME_O", data[1])
        schemadata = schemadata.replace("T1_OS_LOG_O", data[2])
        schemadata = schemadata.replace("T1_OS_STATE_O", data[3])
    with open("./fast/env/server.hsconf.preprodfe", 'w') as schema_file:
        schema_file.write(schemadata)
    with  open("./fast/bin/runawsschema.sh", 'r') as new_file:
        check = "OS_STATE_PASSWD"
        value = ""
        data = ""
        finalfile = ""
        filedata = new_file.read()
        for line in (filedata.split("\n")):
            if check in line:
                data = line
                print data
                value = data + "\n" + schema
                print value
        if value not in filedata:
            finalfile = filedata.replace(data, value)
            with  open("./fast/bin/runawsschema.sh", 'w') as new_file:
                new_file.write(finalfile)

def lifetimerunscemachange(schema):
    #print schema
    data=schema.split(",")
    osadmin = 'editfile  '+ '\"T1_OS_ADMIN_L\"' +"  "+ '\"' +data[0]+'\"'
    osruntime= 'editfile  '+ '\"T1_OS_RUNTIME_L\"' +"  "+ '\"' +data[1]+'\"'
    oslog = 'editfile  '+ '\"T1_OS_LOG_L\"' +"  "+ '\"' +data[2]+'\"'
    osstate = 'editfile  ' + '\"T1_OS_STATE_L\"' + "  " + '\"' + data[3] + '\"'
    schema=" "+osadmin+"\n"+" "+osruntime+"\n"+" "+oslog+"\n"+" "+osstate+"\n"
    with  open("./fast/env/server.hsconf.lifetime", 'r') as schema_file:
        schemadata=schema_file.read()
        schemadata=schemadata.replace("T1_OS_ADMIN_L",data[0])
        schemadata = schemadata.replace("T1_OS_RUNTIME_L", data[1])
        schemadata = schemadata.replace("T1_OS_LOG_L", data[2])
        schemadata = schemadata.replace("T1_OS_STATE_L", data[3])
    with open("./fast/env/server.hsconf.lifetime", 'w') as schema_file:
        schema_file.write(schemadata)
    with  open("./fast/bin/runawsschema.sh", 'r') as new_file:
        check="OS_STATE_PASSWD"
        value=""
        data=""
        finalfile=""
        filedata=new_file.read()
        for line in (filedata.split("\n")):
            if check in line:
                data=line
                print data
                value= data+"\n"+schema
                print value
        if value not  in filedata:
            finalfile=filedata.replace(data,value)
            with  open("./fast/bin/runawsschema.sh", 'w') as new_file:
                new_file.write(finalfile)



   # print schema


def runtablechange(table):
    print "This is my test"

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    import sys
    print sys.argv
    if sys.argv[1] and sys.argv[2] != "":
        if sys.argv[1] == 'devschema':
            devrunscemachange(sys.argv[2])
        elif sys.argv[1] == 'lifeschema':
            lifetimerunscemachange(sys.argv[2])
        elif sys.argv[1] == 'stgschema':
            stgrunscemachange(sys.argv[2])
        elif sys.argv[1] == 'prodschema':
            prodrunscemachange(sys.argv[2])
        elif sys.argv[1] == 'preprodschema':
            preprodrunscemachange(sys.argv[2])
    else:
        print "check the syntax, schema changes not done "

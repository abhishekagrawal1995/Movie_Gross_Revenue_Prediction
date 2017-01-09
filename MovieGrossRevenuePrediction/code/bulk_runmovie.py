import os
import sys
import time
def main():

    
    pythonfilename='scrape_data_v7.py'
    ww = pythonfilename.split('.')
    generalLogFilename = ww[0]
    startyear = 2015
    endyear = 2015
    yearlist = list(range(startyear,endyear+1))

    for year in yearlist:
        begin = 1
        window = 10
        for i in range(1,21):
            startid = begin
            endid = startid + window - 1
            logfilename = '../logs/'+generalLogFilename+'_'+str(year)+'_'+str(startid)+'_'+str(endid)+'.log'
            command = 'nohup time python -u '+pythonfilename+' '+str(year)+' '+str(startid)+' '+str(endid)+' > '+logfilename+' &'
            print command
            os.system(command)
            begin = endid+1
            time.sleep(40)

        break
        time.sleep(180)
        print "done"

if __name__=="__main__":
    main()

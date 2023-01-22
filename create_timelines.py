import DaVinciResolveScript as dvr

#when using the console on the free version
#use the line below
resolve = app.GetResolve()

pm = resolve.GetProjectManager()
proj = pm.GetCurrentProject()
media = proj.GetMediaPool()
storage = resolve.GetMediaStorage()



cliplist = media.GetRootFolder().GetClipList()

tl=format(1,'03d')

#tl=format(1+1,'03d')
num=1
for i in cliplist:
    media.CreateTimelineFromClips(tl,i)
    print("Timeline created for clip number - ",tl)
    tl=format(1+num,'03d')
    num+=1


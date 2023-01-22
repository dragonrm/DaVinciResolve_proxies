#!/usr/bin/env python

# I did not write this 
# props for this script go to FinnJaeger as I found his script on this thread https://forum.blackmagicdesign.com/viewtopic.php?f=21&t=134823
# his repo is here - https://github.com/finnschi/renderalltimelines
# I did make a few changes so that this script will run in the free version by pasting in to the python console.

#change the below setup for DaVinci as needed by your enviroment
import DaVinciResolveScript as dvr
import sys
import time


def AddTimelineToRender(project, timeline, presetName):
    project.SetCurrentTimeline(timeline)
    project.LoadRenderPreset(presetName)

    project.SetRenderSettings({"SelectAllFrames": 1})
    return project.AddRenderJob()


def RenderAllTimelines(resolve, presetName):
    projectManager = resolve.GetProjectManager()
    project = projectManager.GetCurrentProject()
    if not project:
        return False

    resolve.OpenPage("Deliver")
    timelineCount = project.GetTimelineCount()

    for index in range(0, int(timelineCount)):
        if not AddTimelineToRender(project, project.GetTimelineByIndex(index + 1), presetName):
            return False
    return project.StartRendering()


def IsRenderingInProgress(resolve):
    projectManager = resolve.GetProjectManager()
    project = projectManager.GetCurrentProject()
    if not project:
        return False

    return project.IsRenderingInProgress()


def WaitForRenderingCompletion(resolve):
    while IsRenderingInProgress(resolve):
        time.sleep(1)
    return

def DeleteAllRenderJobs(resolve):
    projectManager = resolve.GetProjectManager()
    project = projectManager.GetCurrentProject()
    project.DeleteAllRenderJobs()
    return


# Inputs:
# - preset name for rendering

# if len(sys.argv) < 1:
#     print(
#         "input parameters for scripts are [render preset name]")
#     sys.exit()

##########################################################
######## Changes below need to be checked for your environment
##########################################################

#------- If you are running as an external script you can uncomment the line below and comment out the line below that --------------
#renderPresetName = sys.argv[1]
renderPresetName = "1080Proxies"

#####-------------- Depending on your envorment setup you can uncomment the line below if you are using the Studio version
#------------------ and running external scripts
# Get currently open project
#resolve = GetResolve()

### Running this from the Studio version ######
#resolve = dvr.scriptapp('Resolve')

#####Running from the standard version in the console #####
resolve = app.GetResolve()


if not RenderAllTimelines(resolve, renderPresetName):
    print("Unable to set all timelines for rendering")
    sys.exit()

WaitForRenderingCompletion(resolve)

DeleteAllRenderJobs(resolve)

print("Rendering is completed.")

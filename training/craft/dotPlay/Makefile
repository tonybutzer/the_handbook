DOT=dot -Tsvg
DOTP=dot -Tpng
DOTS = odcT1.dot
DOTSVG = odcT1.svg
DOTPNG = odcT1.png scienceApplications.png architectureStudies.png notionalArchitecture.png unixExample.png paperOutline.png lcmapOrchestration.png lcmapIWDS.png key.png antipatterns.png codeSmellsComplexity.png codeSmellsOOP.png codeSmellsStyle.png studentExample.png roadMap.png tonyCurrent.png dataarray.png datacube_classes.png genericAppMemory.png xarrayApplication.png jobFunctionsTony.png app1.png app2.png app3.png app4.png app5.png app6.png odcTeam.png odcMinimal.png lcmapMinimal.png lcmapOverOdcMinimal.png sprintRoadmap.png appODC1.png

%.svg: %.dot
	$(DOT) -o $@ $<

%.png: %.dot
	$(DOTP) -o $@ $<

#.PHONY: dot
#dot: $(DOTSVG) 

.PHONY: dot2
dot2: $(DOTPNG)

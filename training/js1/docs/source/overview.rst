.. javascript and STAC

STAC the COGs
=============

This documentation represents a living document for the USGS ODC Collaboration initiative formalized as the Task Plan 114 -- subtask titled 

* "Open Data Cube and LCMAP technologies special study including derived science products from ARD (see LSIS PWBS) (FY2019 Q1)"
* This particular github repo is for integrating STAC metadata into ODC Flows

Objectives
++++++++++

1. Undserstand STAC
2. Index STAC using ODC-lite (little-cloud)

Suggested Activities:
+++++++++++++++++++++

**TBD rewrite these**

1. Integrate development teams between Geoscence Australia and the USGS EROS LPIP Teams
2. Provide data and supporting engineering for use by the Open Data Cube Community
3. Pilot test Open Data Cube in several infrastructure ecosystems
4. Validate cloud approaches for "data lake" storage
5. Develop "self-directed" work plans and strategies to maximize the impact of the Open Data Cube **research** activities using an **immersive approach**
6. Foster relationships and develop team charters that cross projects from LSAA and LPIP
7. Develop, promote and explain lean methods for configuring, provisioning and deploying cloud infrastructure via Infrastructure as Code methodologies
8. Develop objective and subjective methods for evaluating software and hardware systems and present findings to peers and customers.
9. Participate on the ODC **Steering Council** and foster effective processes and practices.
10. Test LCMAP algorithms (pyccd first) running on top of the Open Data Cube framework/libraries
11. Demonstrate and expose time-series and pixel level visualizations to the LSAA and Data Science elements at EROS
12. Develop an ODC Engineering Handbook
13. Develop automated data delivery tools for ordering, delivering, unpacking and cloud optimizing Landsat Level1 and Level 2 data from USGS EROS Data Ordering Systems
14. Participate in GA, USGS Collaboration Teleconferences and update high level work plans in **Confluence**
15. Organize the work plan, technology plan and study findings in a set of web based documentation using ODC documentation methods. **This website**


```
DCA-1-2 USGS and GA to test STAC plus COGs in ODC Sandbox   
USGS working on creating STAC records from MTL metadata 
```


Vision - Desired End State
++++++++++++++++++++++++++


> STAC - "metadata made easy"



> Landsat DataLake - "Analysis Ready Data - we got it - bring your science to our data"






1. One billion STAC records
    - eight million L1 scenes
    - eight million L2 scenes
    - metadata for each
        - STAC
        - MTL
        - xml?
2. ODC READY
    - STAC --> Elastic Search
    - COGs for raster imagery
        - Enables a vast variety of scientific visualizations
        - Enables scientific models - pyccd, WoFS, NDVI change detection, machine-learning-TBD
        - CODE REUSE
            - sat-api
            - cumulus
            - STAC ready to run - browsers, tools etc
            - ODC plus XARRAY applications
        - Browser exploitable



Mission
+++++++

to stand-up a Landsat cloud storage dataLake that people will love and use

    AWS S3
        us-west region






Tour of the Infrastructure

    on-prem KVM machines
    SGT instances eng1, odc1



Prior Art

Demo of ODC-lite, elastic, kibana

Demo of STAC creation

Action Plan/WBS
+++++++++++++++

* Refresh the California cloud dataLake - Pieschke
        - with STAC alongside the xml and MTL(s) ? - Hedman
        - when?
* Modify ODC-lite for STAC (python code) - Butzer

* THE END

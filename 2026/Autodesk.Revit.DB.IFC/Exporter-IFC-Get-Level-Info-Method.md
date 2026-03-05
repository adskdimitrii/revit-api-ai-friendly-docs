# Exporter IFC Get Level Info Method

Source: https://www.revitapidocs.com/2026/c404ab36-866c-8ac8-a8b1-c60d963791ed.htm

---

| Exporter IFC Get Level Info Method |
| --- |

**Note: This API is now obsolete.** 

Returns an object representing the information about a level in the document. 
**Namespace:** [Autodesk.Revit.DB.IFC](../ungrouped/Autodesk.-Revit.-DB.-IFC-Namespace.md) 
**Assembly:** RevitAPIIFC (in RevitAPIIFC.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
[ObsoleteAttribute("This is deprecated in Revit 2026.  Use ExporterCacheManager.LevelInfoCache.LevelsById instead.")]
public IFCLevelInfo GetLevelInfo(
	ElementId levelId
)
```

```
<ObsoleteAttribute("This is deprecated in Revit 2026.  Use ExporterCacheManager.LevelInfoCache.LevelsById instead.")>
Public Function GetLevelInfo ( 
	levelId As ElementId
) As IFCLevelInfo
```

```
public:
[ObsoleteAttribute(L"This is deprecated in Revit 2026.  Use ExporterCacheManager.LevelInfoCache.LevelsById instead.")]
IFCLevelInfo^ GetLevelInfo(
	ElementId^ levelId
)
```

```
[<ObsoleteAttribute("This is deprecated in Revit 2026.  Use ExporterCacheManager.LevelInfoCache.LevelsById instead.")>]
member GetLevelInfo : 
        levelId : ElementId -> IFCLevelInfo 
```

#### Parameters

levelId [ElementId](../Autodesk.Revit.DB/Element-Id-Class.md)
:   The level id.

#### Return Value

[IFCLevelInfo](9f287338-fe0c-383b-58be-39105d704a9f.htm) 
The level information. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks Level information is currently automatically collected and cached in the ExporterIFC
 object. This method returns the cached information for a given level,
 which is often needed during export of particular building elements which reference levels, as well
 as to implement automatic wall and column splitting. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[ExporterIFC Class](Exporter-IFC-Class.md) [Autodesk.Revit.DB.IFC Namespace](../ungrouped/Autodesk.-Revit.-DB.-IFC-Namespace.md)

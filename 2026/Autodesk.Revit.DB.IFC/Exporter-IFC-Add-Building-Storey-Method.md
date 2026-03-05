# Exporter IFC Add Building Storey Method

Source: https://www.revitapidocs.com/2026/08c5605c-b66f-baae-5684-d9dc7cf7121a.htm

---

| Exporter IFC Add Building Storey Method |
| --- |

**Note: This API is now obsolete.** 

Adds building storey to the exporter's internal cache. 
**Namespace:** [Autodesk.Revit.DB.IFC](../ungrouped/Autodesk.-Revit.-DB.-IFC-Namespace.md) 
**Assembly:** RevitAPIIFC (in RevitAPIIFC.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
[ObsoleteAttribute("This is deprecated in Revit 2026.  Use ExporterCacheManager.LevelInfoCache.LevelsById instead.")]
public void AddBuildingStorey(
	ElementId id,
	IFCLevelInfo levelInfo
)
```

```
<ObsoleteAttribute("This is deprecated in Revit 2026.  Use ExporterCacheManager.LevelInfoCache.LevelsById instead.")>
Public Sub AddBuildingStorey ( 
	id As ElementId,
	levelInfo As IFCLevelInfo
)
```

```
public:
[ObsoleteAttribute(L"This is deprecated in Revit 2026.  Use ExporterCacheManager.LevelInfoCache.LevelsById instead.")]
void AddBuildingStorey(
	ElementId^ id, 
	IFCLevelInfo^ levelInfo
)
```

```
[<ObsoleteAttribute("This is deprecated in Revit 2026.  Use ExporterCacheManager.LevelInfoCache.LevelsById instead.")>]
member AddBuildingStorey : 
        id : ElementId * 
        levelInfo : IFCLevelInfo -> unit 
```

#### Parameters

id [ElementId](../Autodesk.Revit.DB/Element-Id-Class.md)
:   The level id.

levelInfo [IFCLevelInfo](9f287338-fe0c-383b-58be-39105d704a9f.htm)
:   The IFCLevelInfo object.

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[ExporterIFC Class](Exporter-IFC-Class.md) [Autodesk.Revit.DB.IFC Namespace](../ungrouped/Autodesk.-Revit.-DB.-IFC-Namespace.md)

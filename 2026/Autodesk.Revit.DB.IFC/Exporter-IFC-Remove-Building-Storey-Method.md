# Exporter IFC Remove Building Storey Method

Source: https://www.revitapidocs.com/2026/e1dada57-54f4-ecbb-d3bf-75144f65c34e.htm

---

| Exporter IFC Remove Building Storey Method |
| --- |

**Note: This API is now obsolete.** 

Removes an IFCLevelInfo corresponding to a level from the exporter's internal cache. 
**Namespace:** [Autodesk.Revit.DB.IFC](../ungrouped/Autodesk.-Revit.-DB.-IFC-Namespace.md) 
**Assembly:** RevitAPIIFC (in RevitAPIIFC.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
[ObsoleteAttribute("This is deprecated in Revit 2026.  Use ExporterCacheManager.LevelInfoCache.LevelsById instead.")]
public void RemoveBuildingStorey(
	ElementId id
)
```

```
<ObsoleteAttribute("This is deprecated in Revit 2026.  Use ExporterCacheManager.LevelInfoCache.LevelsById instead.")>
Public Sub RemoveBuildingStorey ( 
	id As ElementId
)
```

```
public:
[ObsoleteAttribute(L"This is deprecated in Revit 2026.  Use ExporterCacheManager.LevelInfoCache.LevelsById instead.")]
void RemoveBuildingStorey(
	ElementId^ id
)
```

```
[<ObsoleteAttribute("This is deprecated in Revit 2026.  Use ExporterCacheManager.LevelInfoCache.LevelsById instead.")>]
member RemoveBuildingStorey : 
        id : ElementId -> unit 
```

#### Parameters

id [ElementId](../Autodesk.Revit.DB/Element-Id-Class.md)
:   The level id.

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[ExporterIFC Class](Exporter-IFC-Class.md) [Autodesk.Revit.DB.IFC Namespace](../ungrouped/Autodesk.-Revit.-DB.-IFC-Namespace.md)

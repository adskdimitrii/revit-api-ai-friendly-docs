# Exporter IFCUtils Get Num Building Storeys Method

Source: https://www.revitapidocs.com/2026/c6bdcbc0-4c99-237b-ea4d-a243d38b819a.htm

---

| Exporter IFCUtils Get Num Building Storeys Method |
| --- |

**Note: This API is now obsolete.** 

Returns the number of non\-empty, non\-duplicate building stories in the file. 
**Namespace:** [Autodesk.Revit.DB.IFC](../ungrouped/Autodesk.-Revit.-DB.-IFC-Namespace.md) 
**Assembly:** RevitAPIIFC (in RevitAPIIFC.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
[ObsoleteAttribute("This is deprecated in Revit 2026.  Use ExporterCacheManager.LevelInfoCache.LevelsById.Count instead.")]
public static int GetNumBuildingStoreys(
	ExporterIFC exporterIFC
)
```

```
<ObsoleteAttribute("This is deprecated in Revit 2026.  Use ExporterCacheManager.LevelInfoCache.LevelsById.Count instead.")>
Public Shared Function GetNumBuildingStoreys ( 
	exporterIFC As ExporterIFC
) As Integer
```

```
public:
[ObsoleteAttribute(L"This is deprecated in Revit 2026.  Use ExporterCacheManager.LevelInfoCache.LevelsById.Count instead.")]
static int GetNumBuildingStoreys(
	ExporterIFC^ exporterIFC
)
```

```
[<ObsoleteAttribute("This is deprecated in Revit 2026.  Use ExporterCacheManager.LevelInfoCache.LevelsById.Count instead.")>]
static member GetNumBuildingStoreys : 
        exporterIFC : ExporterIFC -> int 
```

#### Parameters

exporterIFC [ExporterIFC](Exporter-IFC-Class.md)
:   The exporter.

#### Return Value

Int32 
The number of stories. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[ExporterIFCUtils Class](Exporter-IFCUtils-Class.md) [Autodesk.Revit.DB.IFC Namespace](../ungrouped/Autodesk.-Revit.-DB.-IFC-Namespace.md)

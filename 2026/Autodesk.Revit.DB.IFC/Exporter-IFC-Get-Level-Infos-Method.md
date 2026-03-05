# Exporter IFC Get Level Infos Method

Source: https://www.revitapidocs.com/2026/c7f1c52a-a0d0-cc15-4a08-1c476bb7509b.htm

---

| Exporter IFC Get Level Infos Method |
| --- |

**Note: This API is now obsolete.** 

Returns a collection containing the information about all levels in the document. 
**Namespace:** [Autodesk.Revit.DB.IFC](../ungrouped/Autodesk.-Revit.-DB.-IFC-Namespace.md) 
**Assembly:** RevitAPIIFC (in RevitAPIIFC.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
[ObsoleteAttribute("This is deprecated in Revit 2026.  Use ExporterCacheManager.LevelInfoCache.LevelsById instead.")]
public IDictionary<ElementId, IFCLevelInfo> GetLevelInfos()
```

```
<ObsoleteAttribute("This is deprecated in Revit 2026.  Use ExporterCacheManager.LevelInfoCache.LevelsById instead.")>
Public Function GetLevelInfos As IDictionary(Of ElementId, IFCLevelInfo)
```

```
public:
[ObsoleteAttribute(L"This is deprecated in Revit 2026.  Use ExporterCacheManager.LevelInfoCache.LevelsById instead.")]
IDictionary<ElementId^, IFCLevelInfo^>^ GetLevelInfos()
```

```
[<ObsoleteAttribute("This is deprecated in Revit 2026.  Use ExporterCacheManager.LevelInfoCache.LevelsById instead.")>]
member GetLevelInfos : unit -> IDictionary<ElementId, IFCLevelInfo> 
```

#### Return Value

IDictionary [ElementId](../Autodesk.Revit.DB/Element-Id-Class.md) , [IFCLevelInfo](9f287338-fe0c-383b-58be-39105d704a9f.htm) 
The collection of level information. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks Level information is currently automatically collected and cached in the ExporterIFC
 object. This method returns the cached information which is often needed during export
 of particular building elements which reference levels, as well as to implement automatic
 wall and column splitting. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[ExporterIFC Class](Exporter-IFC-Class.md) [Autodesk.Revit.DB.IFC Namespace](../ungrouped/Autodesk.-Revit.-DB.-IFC-Namespace.md)

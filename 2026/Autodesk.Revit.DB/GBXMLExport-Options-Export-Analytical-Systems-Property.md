# GBXMLExport Options Export Analytical Systems Property

Source: https://www.revitapidocs.com/2026/f28f66f7-8c0a-0037-dade-20452bfbca9a.htm

---

| GBXMLExport Options Export Analytical Systems Property |
| --- |

**Note: This API is now obsolete.** 

Indicates if the gbXML should contain analytical system elements (e.g., Water Loop, Air System, and Zone Equipment). 
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
[ObsoleteAttribute("This method is deprecated in Revit 2026 and may be removed in a later version of Revit. Revit will always export AnalyticalSystems at that point.")]
public bool ExportAnalyticalSystems { get; set; }
```

```
<ObsoleteAttribute("This method is deprecated in Revit 2026 and may be removed in a later version of Revit. Revit will always export AnalyticalSystems at that point.")>
Public Property ExportAnalyticalSystems As Boolean
	Get
	Set
```

```
public:
[ObsoleteAttribute(L"This method is deprecated in Revit 2026 and may be removed in a later version of Revit. Revit will always export AnalyticalSystems at that point.")]
property bool ExportAnalyticalSystems {
	bool get ();
	void set (bool value);
}
```

```
[<ObsoleteAttribute("This method is deprecated in Revit 2026 and may be removed in a later version of Revit. Revit will always export AnalyticalSystems at that point.")>]
member ExportAnalyticalSystems : bool with get, set
```

#### Property Value

Boolean ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[GBXMLExportOptions Class](GBXMLExport-Options-Class.md) [Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)

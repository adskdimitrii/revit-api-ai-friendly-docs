# GBXMLExport Options Export Energy Model Type Property

Source: https://www.revitapidocs.com/2026/e0b8443f-e415-271a-5c9f-3c99cca13406.htm

---

| GBXMLExport Options Export Energy Model Type Property |
| --- |

**Note: This API is now obsolete.** 

The energy model type from which gbXML will be exported. 
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
[ObsoleteAttribute("This method is deprecated in Revit 2026 and may be removed in a later version of Revit.")]
public ExportEnergyModelType ExportEnergyModelType { get; set; }
```

```
<ObsoleteAttribute("This method is deprecated in Revit 2026 and may be removed in a later version of Revit.")>
Public Property ExportEnergyModelType As ExportEnergyModelType
	Get
	Set
```

```
public:
[ObsoleteAttribute(L"This method is deprecated in Revit 2026 and may be removed in a later version of Revit.")]
property ExportEnergyModelType ExportEnergyModelType {
	ExportEnergyModelType get ();
	void set (ExportEnergyModelType value);
}
```

```
[<ObsoleteAttribute("This method is deprecated in Revit 2026 and may be removed in a later version of Revit.")>]
member ExportEnergyModelType : ExportEnergyModelType with get, set
```

#### Property Value

[ExportEnergyModelType](a5e9c660-febe-e1c0-af58-47a55bde5443.htm) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | When setting this property: A value passed for an enumeration argument is not a member of that enumeration |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks Default value is AnalysisMode. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[GBXMLExportOptions Class](GBXMLExport-Options-Class.md) [Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)

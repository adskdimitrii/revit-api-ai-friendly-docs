# Energy Analysis Zone CADObject Unique Id Property

Source: https://www.revitapidocs.com/2026/fe873f20-53b4-2d79-6920-c2d333cee635.htm

---

| Energy Analysis Zone CADObject Unique Id Property |
| --- |

The unique id of the originating CAD object (model element) associated with this zone. 
**Namespace:** [Autodesk.Revit.DB.Analysis](../ungrouped/Autodesk.-Revit.-DB.-Analysis-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public string CADObjectUniqueId { get; }
```

```
Public ReadOnly Property CADObjectUniqueId As String
	Get
```

```
public:
property String^ CADObjectUniqueId {
	String^ get ();
}
```

```
member CADObjectUniqueId : string with get
```

#### Property Value

String ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks This id can be passed to obtain the element from Document.Element\[string] property, but any element obtained through this method
 may no longer point to a valid or up\-to\-date model element. The originating CAD object is only accurate and up\-to\-date at the time of creation of the energy model. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[EnergyAnalysisZone Class](Energy-Analysis-Zone-Class.md) [Autodesk.Revit.DB.Analysis Namespace](../ungrouped/Autodesk.-Revit.-DB.-Analysis-Namespace.md)

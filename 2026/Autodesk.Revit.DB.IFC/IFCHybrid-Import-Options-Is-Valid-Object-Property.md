# IFCHybrid Import Options Is Valid Object Property

Source: https://www.revitapidocs.com/2026/6ba69b39-abb0-3c7d-770d-6d985c3eb477.htm

---

| IFCHybrid Import Options Is Valid Object Property |
| --- |

Specifies whether the .NET object represents a valid Revit entity. 
**Namespace:** [Autodesk.Revit.DB.IFC](../ungrouped/Autodesk.-Revit.-DB.-IFC-Namespace.md) 
**Assembly:** RevitAPIIFC (in RevitAPIIFC.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public bool IsValidObject { get; }
```

```
Public ReadOnly Property IsValidObject As Boolean
	Get
```

```
public:
property bool IsValidObject {
	bool get ();
}
```

```
member IsValidObject : bool with get
```

#### Return Value

Boolean 
True if the API object holds a valid Revit native object, false otherwise. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks If the corresponding Revit native object is destroyed, or creation of the corresponding object is undone,
 a managed API object containing it is no longer valid. API methods cannot be called on invalidated wrapper objects. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[IFCHybridImportOptions Class](IFCHybrid-Import-Options-Class.md) [Autodesk.Revit.DB.IFC Namespace](../ungrouped/Autodesk.-Revit.-DB.-IFC-Namespace.md)

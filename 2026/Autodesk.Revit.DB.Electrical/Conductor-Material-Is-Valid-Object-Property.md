# Conductor Material Is Valid Object Property

Source: https://www.revitapidocs.com/2026/3055f745-ede9-0bb4-81d1-1ba35200a837.htm

---

| Conductor Material Is Valid Object Property |
| --- |

Specifies whether the .NET object represents a valid Revit entity. 
**Namespace:** [Autodesk.Revit.DB.Electrical](../ungrouped/Autodesk.-Revit.-DB.-Electrical-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
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

[ConductorMaterial Class](Conductor-Material-Class.md) [Autodesk.Revit.DB.Electrical Namespace](../ungrouped/Autodesk.-Revit.-DB.-Electrical-Namespace.md)

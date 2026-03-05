# Nurb Spline Ctrl Points Property

Source: https://www.revitapidocs.com/2026/7137825e-3588-b3ee-a477-477151723a3e.htm

---

| Nurb Spline Ctrl Points Property |
| --- |

Returns the control points of the nurb spline. 
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public IList<XYZ> CtrlPoints { get; }
```

```
Public ReadOnly Property CtrlPoints As IList(Of XYZ)
	Get
```

```
public:
property IList<XYZ^>^ CtrlPoints {
	IList<XYZ^>^ get ();
}
```

```
member CtrlPoints : IList<XYZ> with get
```

#### Property Value

IList [XYZ](c2fd995c-95c0-58fb-f5de-f3246cbc5600.htm) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks This method returns a copy of the internally\-managed data. 
 Repeated access of this property will return a new copy each time, which may be inefficient. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[NurbSpline Class](Nurb-Spline-Class.md) [Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)

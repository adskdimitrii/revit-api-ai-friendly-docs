# Electrical System Hot Conductor Size Property

Source: https://www.revitapidocs.com/2026/15b83037-f5d7-4f4d-70bf-968c65b517d4.htm

---

| Electrical System Hot Conductor Size Property |
| --- |

The size of a Hot Conductor in the Electrical System. 
**Namespace:** [Autodesk.Revit.DB.Electrical](../ungrouped/Autodesk.-Revit.-DB.-Electrical-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public ElementId HotConductorSize { get; }
```

```
Public ReadOnly Property HotConductorSize As ElementId
	Get
```

```
public:
property ElementId^ HotConductorSize {
	ElementId^ get ();
}
```

```
member HotConductorSize : ElementId with get
```

#### Property Value

[ElementId](../Autodesk.Revit.DB/Element-Id-Class.md) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | This property only available when System Type is Power! |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks Each Hot Conductor has the same size in the Electrical System. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[ElectricalSystem Class](Electrical-System-Class.md) [Autodesk.Revit.DB.Electrical Namespace](../ungrouped/Autodesk.-Revit.-DB.-Electrical-Namespace.md)

# Electrical System Ground Conductor Size Property

Source: https://www.revitapidocs.com/2026/4a5296f4-064c-9298-3e19-05a6cbd87bf5.htm

---

| Electrical System Ground Conductor Size Property |
| --- |

The size of a Ground Conductor in the Electrical System. 
**Namespace:** [Autodesk.Revit.DB.Electrical](../ungrouped/Autodesk.-Revit.-DB.-Electrical-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public ElementId GroundConductorSize { get; }
```

```
Public ReadOnly Property GroundConductorSize As ElementId
	Get
```

```
public:
property ElementId^ GroundConductorSize {
	ElementId^ get ();
}
```

```
member GroundConductorSize : ElementId with get
```

#### Property Value

[ElementId](../Autodesk.Revit.DB/Element-Id-Class.md) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | This property only available when System Type is Power! |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks Each Ground Conductor has the same size in the Electrical System. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[ElectricalSystem Class](Electrical-System-Class.md) [Autodesk.Revit.DB.Electrical Namespace](../ungrouped/Autodesk.-Revit.-DB.-Electrical-Namespace.md)

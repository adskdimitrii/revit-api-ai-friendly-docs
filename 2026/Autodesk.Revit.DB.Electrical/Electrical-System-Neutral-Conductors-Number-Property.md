# Electrical System Neutral Conductors Number Property

Source: https://www.revitapidocs.com/2026/9f62c1f5-a9c9-16ee-e891-81171f131fc7.htm

---

| Electrical System Neutral Conductors Number Property |
| --- |

The NeutralConductors Number of the Electrical System. 
**Namespace:** [Autodesk.Revit.DB.Electrical](../ungrouped/Autodesk.-Revit.-DB.-Electrical-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public int NeutralConductorsNumber { get; }
```

```
Public ReadOnly Property NeutralConductorsNumber As Integer
	Get
```

```
public:
property int NeutralConductorsNumber {
	int get ();
}
```

```
member NeutralConductorsNumber : int with get
```

#### Property Value

Int32 ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | This property only available when System Type is Power! |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks This property is used to retrieve the NeutralConductors Number of the Electrical System. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[ElectricalSystem Class](Electrical-System-Class.md) [Autodesk.Revit.DB.Electrical Namespace](../ungrouped/Autodesk.-Revit.-DB.-Electrical-Namespace.md)

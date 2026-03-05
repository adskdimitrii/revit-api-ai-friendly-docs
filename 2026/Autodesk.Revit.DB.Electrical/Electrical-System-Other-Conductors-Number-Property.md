# Electrical System Other Conductors Number Property

Source: https://www.revitapidocs.com/2026/e08b1ded-65f8-4871-e3bb-a058f0b28a87.htm

---

| Electrical System Other Conductors Number Property |
| --- |

The OtherConductors Number of the Electrical System. 
**Namespace:** [Autodesk.Revit.DB.Electrical](../ungrouped/Autodesk.-Revit.-DB.-Electrical-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public int OtherConductorsNumber { get; }
```

```
Public ReadOnly Property OtherConductorsNumber As Integer
	Get
```

```
public:
property int OtherConductorsNumber {
	int get ();
}
```

```
member OtherConductorsNumber : int with get
```

#### Property Value

Int32 ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | This property only available when System Type is Power! |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks This property is used to retrieve the OtherConductors Number of the Electrical System. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[ElectricalSystem Class](Electrical-System-Class.md) [Autodesk.Revit.DB.Electrical Namespace](../ungrouped/Autodesk.-Revit.-DB.-Electrical-Namespace.md)

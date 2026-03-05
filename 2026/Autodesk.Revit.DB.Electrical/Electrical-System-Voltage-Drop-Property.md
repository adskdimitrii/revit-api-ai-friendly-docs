# Electrical System Voltage Drop Property

Source: https://www.revitapidocs.com/2026/2f7d179a-a6c3-375b-d184-cc796e918f5d.htm

---

| Electrical System Voltage Drop Property |
| --- |

**Note: This API is now obsolete.** 

The VoltageDrop value of the Electrical System. 
**Namespace:** [Autodesk.Revit.DB.Electrical](../ungrouped/Autodesk.-Revit.-DB.-Electrical-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
[ObsoleteAttribute("This property is deprecated in Revit 2026 and may be removed in a future version of Revit. There is no replacement for this property because Revit no longer supports this.")]
public double VoltageDrop { get; }
```

```
<ObsoleteAttribute("This property is deprecated in Revit 2026 and may be removed in a future version of Revit. There is no replacement for this property because Revit no longer supports this.")>
Public ReadOnly Property VoltageDrop As Double
	Get
```

```
public:
[ObsoleteAttribute(L"This property is deprecated in Revit 2026 and may be removed in a future version of Revit. There is no replacement for this property because Revit no longer supports this.")]
property double VoltageDrop {
	double get ();
}
```

```
[<ObsoleteAttribute("This property is deprecated in Revit 2026 and may be removed in a future version of Revit. There is no replacement for this property because Revit no longer supports this.")>]
member VoltageDrop : float with get
```

#### Property Value

Double ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | This property only available when System Type is Power! |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks This property is used to retrieve the VoltageDrop value of the Electrical System. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[ElectricalSystem Class](Electrical-System-Class.md) [Autodesk.Revit.DB.Electrical Namespace](../ungrouped/Autodesk.-Revit.-DB.-Electrical-Namespace.md)

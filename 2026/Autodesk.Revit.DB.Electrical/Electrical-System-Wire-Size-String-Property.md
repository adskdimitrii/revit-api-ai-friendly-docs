# Electrical System Wire Size String Property

Source: https://www.revitapidocs.com/2026/51fad9c3-b6a4-a8b3-95b2-beafff72f994.htm

---

| Electrical System Wire Size String Property |
| --- |

**Note: This API is now obsolete.** 

The WireSize as a String of the Electrical System 
**Namespace:** [Autodesk.Revit.DB.Electrical](../ungrouped/Autodesk.-Revit.-DB.-Electrical-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
[ObsoleteAttribute("This property is deprecated in Revit 2026 and may be removed in a future version of Revit. Please use CableSize instead. CableSize will be set on ElectricalSystem properly during document upgrade.")]
public string WireSizeString { get; }
```

```
<ObsoleteAttribute("This property is deprecated in Revit 2026 and may be removed in a future version of Revit. Please use CableSize instead. CableSize will be set on ElectricalSystem properly during document upgrade.")>
Public ReadOnly Property WireSizeString As String
	Get
```

```
public:
[ObsoleteAttribute(L"This property is deprecated in Revit 2026 and may be removed in a future version of Revit. Please use CableSize instead. CableSize will be set on ElectricalSystem properly during document upgrade.")]
property String^ WireSizeString {
	String^ get ();
}
```

```
[<ObsoleteAttribute("This property is deprecated in Revit 2026 and may be removed in a future version of Revit. Please use CableSize instead. CableSize will be set on ElectricalSystem properly during document upgrade.")>]
member WireSizeString : string with get
```

#### Property Value

String ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | This property only available when System Type is Power! |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks This property is used to retrieve the WireSize String of the Electrical System. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[ElectricalSystem Class](Electrical-System-Class.md) [Autodesk.Revit.DB.Electrical Namespace](../ungrouped/Autodesk.-Revit.-DB.-Electrical-Namespace.md)

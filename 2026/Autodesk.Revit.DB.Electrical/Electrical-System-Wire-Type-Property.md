# Electrical System Wire Type Property

Source: https://www.revitapidocs.com/2026/d605965d-bbed-c3c9-14fa-2d040ec76dca.htm

---

| Electrical System Wire Type Property |
| --- |

**Note: This API is now obsolete.** 

The wire type of the Electrical System. 
**Namespace:** [Autodesk.Revit.DB.Electrical](../ungrouped/Autodesk.-Revit.-DB.-Electrical-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
[ObsoleteAttribute("This property is deprecated in Revit 2026 and may be removed in a future version of Revit. Please use CableType instead. CableType will be set on ElectricalSystem properly during document upgrade.")]
public WireType WireType { get; set; }
```

```
<ObsoleteAttribute("This property is deprecated in Revit 2026 and may be removed in a future version of Revit. Please use CableType instead. CableType will be set on ElectricalSystem properly during document upgrade.")>
Public Property WireType As WireType
	Get
	Set
```

```
public:
[ObsoleteAttribute(L"This property is deprecated in Revit 2026 and may be removed in a future version of Revit. Please use CableType instead. CableType will be set on ElectricalSystem properly during document upgrade.")]
property WireType^ WireType {
	WireType^ get ();
	void set (WireType^ value);
}
```

```
[<ObsoleteAttribute("This property is deprecated in Revit 2026 and may be removed in a future version of Revit. Please use CableType instead. CableType will be set on ElectricalSystem properly during document upgrade.")>]
member WireType : WireType with get, set
```

#### Property Value

[WireType](Wire-Type-Class.md) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | When setting this property: A non\-optional argument was null |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks This property is used to retrieve the wire type of the Electrical System. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[ElectricalSystem Class](Electrical-System-Class.md) [Autodesk.Revit.DB.Electrical Namespace](../ungrouped/Autodesk.-Revit.-DB.-Electrical-Namespace.md)

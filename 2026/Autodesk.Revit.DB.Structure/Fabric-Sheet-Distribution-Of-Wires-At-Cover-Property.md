# Fabric Sheet Distribution Of Wires At Cover Property

Source: https://www.revitapidocs.com/2026/d0ff8f7e-8c8f-4bfa-b0ab-ac3d8514140e.htm

---

| Fabric Sheet Distribution Of Wires At Cover Property |
| --- |

The distribution of wires that is closest to the cover. 
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public WireDistributionDirection DistributionOfWiresAtCover { get; set; }
```

```
Public Property DistributionOfWiresAtCover As WireDistributionDirection
	Get
	Set
```

```
public:
property WireDistributionDirection DistributionOfWiresAtCover {
	WireDistributionDirection get ();
	void set (WireDistributionDirection value);
}
```

```
member DistributionOfWiresAtCover : WireDistributionDirection with get, set
```

#### Property Value

[WireDistributionDirection](Wire-Distribution-Direction-Enumeration.md) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | When setting this property: A value passed for an enumeration argument is not a member of that enumeration |
| [InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | When setting this property: This fabric sheet is bent. Method shall be called only for flat fabric sheets. |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks This parameter is only relevant for instances of flat fabric sheets.
 Fabric sheets are created with the Major distribution set at the cover by default. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[FabricSheet Class](Fabric-Sheet-Class.md) [Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)

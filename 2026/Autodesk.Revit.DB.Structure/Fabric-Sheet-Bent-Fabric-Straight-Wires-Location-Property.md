# Fabric Sheet Bent Fabric Straight Wires Location Property

Source: https://www.revitapidocs.com/2026/beb33ed1-b28b-2e4c-2ea3-51ec4bc4f79a.htm

---

| Fabric Sheet Bent Fabric Straight Wires Location Property |
| --- |

Specifies the location of straight bars with respect to bent bars in the fabric sheet. 
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public BentFabricStraightWiresLocation BentFabricStraightWiresLocation { get; set; }
```

```
Public Property BentFabricStraightWiresLocation As BentFabricStraightWiresLocation
	Get
	Set
```

```
public:
property BentFabricStraightWiresLocation BentFabricStraightWiresLocation {
	BentFabricStraightWiresLocation get ();
	void set (BentFabricStraightWiresLocation value);
}
```

```
member BentFabricStraightWiresLocation : BentFabricStraightWiresLocation with get, set
```

#### Property Value

[BentFabricStraightWiresLocation](366283e6-dcb6-d863-13e0-32937d93a499.htm) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | When setting this property: A value passed for an enumeration argument is not a member of that enumeration |
| [InvalidObjectException](8092dec2-113a-0823-1a09-a46c11f99fea.htm) | When setting this property: The data\-setting method is not applicable to fabric sheets that are flat. |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks This parameter applies only to bent fabric sheets.
 The side on wich straight wires will be loacted is determined by the start and end point of the first bent profile segment that specifies the direction of the curve loop on plane. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[FabricSheet Class](Fabric-Sheet-Class.md) [Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)

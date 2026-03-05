# Fabric Sheet Bent Fabric Bend Direction Property

Source: https://www.revitapidocs.com/2026/0a69fdd3-8c45-d097-19c2-fb07a6a8f5cf.htm

---

| Fabric Sheet Bent Fabric Bend Direction Property |
| --- |

Specifies which wire direction of the fabric sheet is bent. 
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public BentFabricBendDirection BentFabricBendDirection { get; set; }
```

```
Public Property BentFabricBendDirection As BentFabricBendDirection
	Get
	Set
```

```
public:
property BentFabricBendDirection BentFabricBendDirection {
	BentFabricBendDirection get ();
	void set (BentFabricBendDirection value);
}
```

```
member BentFabricBendDirection : BentFabricBendDirection with get, set
```

#### Property Value

[BentFabricBendDirection](9de03473-2c8d-840f-d5e6-745a4526e0c4.htm) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentOutOfRangeException](60f148c9-ece0-a6bb-4e12-bb4a9c8c8a24.htm) | When setting this property: A value passed for an enumeration argument is not a member of that enumeration |
| [InvalidObjectException](8092dec2-113a-0823-1a09-a46c11f99fea.htm) | When setting this property: The data\-setting method is not applicable to fabric sheets that are flat. |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks This parameter applies only to bent fabric sheets. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[FabricSheet Class](Fabric-Sheet-Class.md) [Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)

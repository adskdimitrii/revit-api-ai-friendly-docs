# Document New Union Fitting Method

Source: https://www.revitapidocs.com/2026/84596c17-3a5a-74f5-e050-98ab3b15dd5b.htm

---

| Document New Union Fitting Method |
| --- |

Add a new family instance of an union fitting into the Autodesk Revit document,
using two connectors. 
**Namespace:** [Autodesk.Revit.Creation](ded320da-058a-4edd-0418-0582389559a7.htm) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public FamilyInstance NewUnionFitting(
	Connector connector1,
	Connector connector2
)
```

```
Public Function NewUnionFitting ( 
	connector1 As Connector,
	connector2 As Connector
) As FamilyInstance
```

```
public:
FamilyInstance^ NewUnionFitting(
	Connector^ connector1, 
	Connector^ connector2
)
```

```
member NewUnionFitting : 
        connector1 : Connector * 
        connector2 : Connector -> FamilyInstance 
```

#### Parameters

connector1 [Connector](11e07082-b3f2-26a1-de79-16535f44716c.htm)
:   The first connector to be connected to the union.

connector2 [Connector](11e07082-b3f2-26a1-de79-16535f44716c.htm)
:   The second connector to be connected to the union.

#### Return Value

[FamilyInstance](0d2231f8-91e6-794f-92ae-16aad8014b27.htm) 
If creation was successful then a family instance to the new union object is returned,
otherwise an exception with failure information will be thrown. In the case of successful creation 
with another fitting type, may be returned. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | Thrown when the input argument connector1 or connector2 is . |
| [ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | Thrown when the connectors cannot be used for union creation. For example,  they cannot be from the same element, they must be of the same domain and shape,  and the owner of the connector1 should be a (flex) duct or pipe. |
| [InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Thrown when union fitting cannot be created. |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[Document Class](Document-Class.md) [Autodesk.Revit.Creation Namespace](ded320da-058a-4edd-0418-0582389559a7.htm)

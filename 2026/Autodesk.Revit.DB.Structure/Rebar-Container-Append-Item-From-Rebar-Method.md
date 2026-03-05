# Rebar Container Append Item From Rebar Method

Source: https://www.revitapidocs.com/2026/b7e0adc7-0f2e-af1e-9224-3f1ae4067e3c.htm

---

| Rebar Container Append Item From Rebar Method |
| --- |

Appends an Item to the RebarContainer. Fills its data on base of the Rebar.
 Will throw exception if given rebar is not shape driven.
 Will throw exception if given rebar has moved bars in set. 
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public RebarContainerItem AppendItemFromRebar(
	Rebar rebar
)
```

```
Public Function AppendItemFromRebar ( 
	rebar As Rebar
) As RebarContainerItem
```

```
public:
RebarContainerItem^ AppendItemFromRebar(
	Rebar^ rebar
)
```

```
member AppendItemFromRebar : 
        rebar : Rebar -> RebarContainerItem 
```

#### Parameters

rebar [Rebar](Rebar-Class.md)
:   The Rebar.

#### Return Value

[RebarContainerItem](Rebar-Container-Item-Class.md) 
The Rebar Container Item. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | A RebarContainerItem cannot be created from a Free Form Rebar or from a Shape Driven Rebar whose Rebar Shape has End Treatments or Cranks or terminations' rotation angles are different than 0\.  \-or\-  Can't create container from Rebar with moved bars. |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[RebarContainer Class](Rebar-Container-Class.md) [Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)

# Rebar Container Item Set From Rebar Method

Source: https://www.revitapidocs.com/2026/e81c0c0c-c49f-f451-7e13-9495eaba527f.htm

---

| Rebar Container Item Set From Rebar Method |
| --- |

Set an instance of a RebarContainerItem element according to a Rebar parameters.
 Will throw exception if given rebar is not shape driven.
 Will throw exception if given rebar has moved bars in set. 
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public void SetFromRebar(
	Rebar rebar
)
```

```
Public Sub SetFromRebar ( 
	rebar As Rebar
)
```

```
public:
void SetFromRebar(
	Rebar^ rebar
)
```

```
member SetFromRebar : 
        rebar : Rebar -> unit 
```

#### Parameters

rebar [Rebar](Rebar-Class.md)
:   The Rebar.

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | Can't create container from Rebar with moved bars.  \-or\-  Can't create container from Rebar which has excluded bars other than the first and last one.  \-or\-  A RebarContainerItem cannot be created from a Free Form Rebar or from a Shape Driven Rebar whose Rebar Shape has End Treatments or Cranks or terminations' rotation angles are different than 0\. |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[RebarContainerItem Class](Rebar-Container-Item-Class.md) [Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)

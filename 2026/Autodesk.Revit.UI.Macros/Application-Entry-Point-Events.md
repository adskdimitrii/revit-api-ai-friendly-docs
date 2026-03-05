# Application Entry Point Events

Source: https://www.revitapidocs.com/2026/0d295f42-9d0a-af04-0599-6f91aeee2264.htm

---

| Application Entry Point Events |
| --- |

The [ApplicationEntryPoint](Application-Entry-Point-Class.md) type exposes the following members. 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Events 

|  | Name | Description |
| --- | --- | --- |
| ![Public event](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubevent.gif "Public event") | [ApplicationClosing](61068521-c216-3ab5-9d6e-28006fcfe0ae.htm) | Subscribe to the ApplicationClosing event to be notified when the Revit application is just about to be closed. (Inherited from [UIApplication](../Autodesk.Revit.UI/UIApplication-Class.md) ) |
| ![Public event](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubevent.gif "Public event") | [DialogBoxShowing](cb46ea4c-2b80-0ec2-063f-dda6f662948a.htm) | Subscribe to the DialogBoxShowing event to be notified when Revit is just about to show a dialog box or a message box. (Inherited from [UIApplication](../Autodesk.Revit.UI/UIApplication-Class.md) ) |
| ![Public event](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubevent.gif "Public event") | [DisplayingOptionsDialog](7d12db51-950c-b506-f23d-19c1e58bd615.htm) | Subscribe to the options dialog displaying event to be notified when Revit options dialog is displaying. (Inherited from [UIApplication](../Autodesk.Revit.UI/UIApplication-Class.md) ) |
| ![Public event](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubevent.gif "Public event") | [DockableFrameFocusChanged](f007d1f4-e911-60cf-3973-af1007b67ce2.htm) | Subscribe to this event to be notified when a Revit GenericDockableFrame has gained focus or lost focus in the Revit user interface.  This event is called only for API\-created GenericDockableFrames. (Inherited from [UIApplication](../Autodesk.Revit.UI/UIApplication-Class.md) ) |
| ![Public event](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubevent.gif "Public event") | [DockableFrameVisibilityChanged](6ae2552a-6a6c-bc44-515d-8ca7ad7f6ae4.htm) | Subscribe to this event to be notified when a Revit GenericDockableFrame has been shown or hidden in the Revit user interface.  This event is called only for API\-created GenericDockableFrames. (Inherited from [UIApplication](../Autodesk.Revit.UI/UIApplication-Class.md) ) |
| ![Public event](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubevent.gif "Public event") | [FabricationPartBrowserChanged](4b9bd1fa-925a-a5a3-af6c-d7b7b54e3ee7.htm) | Subscribe to MEP Fabrication part browser changed event to be notified when MEP Fabrication part browser is updated. (Inherited from [UIApplication](../Autodesk.Revit.UI/UIApplication-Class.md) ) |
| ![Public event](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubevent.gif "Public event") | [FormulaEditing](ff842cc8-67a9-2c51-843d-d17767e757a8.htm) | Subscribe to the FormulaEditing event to be notified when the edit formula button has been clicked. (Inherited from [UIApplication](../Autodesk.Revit.UI/UIApplication-Class.md) ) |
| ![Public event](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubevent.gif "Public event") | [Idling](56145d84-e948-730a-dc72-2a7b88a50a99.htm) | Subscribe to the Idling event to be notified when Revit is not in an active tool or transaction. (Inherited from [UIApplication](../Autodesk.Revit.UI/UIApplication-Class.md) ) |
| ![Public event](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubevent.gif "Public event") | [MacroUpdated](a301f8e8-e4fa-eef8-0500-3b110a3635f1.htm) | MacroUpdated. (Inherited from [UIApplication](../Autodesk.Revit.UI/UIApplication-Class.md) ) |
| ![Public event](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubevent.gif "Public event") | [SelectionChanged](9ac32ac2-974b-235c-ceea-5d436e5b8e59.htm) | Subscribe to the SelectionChanged event to be notified after the selection was changed. (Inherited from [UIApplication](../Autodesk.Revit.UI/UIApplication-Class.md) ) |
| ![Public event](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubevent.gif "Public event") | [ThemeChanged](1038e6c9-bba1-d0ec-10cf-3a4fcbcc6351.htm) | Subscribe to the ThemeChanged event to be notified after the theme was changed. (Inherited from [UIApplication](../Autodesk.Revit.UI/UIApplication-Class.md) ) |
| ![Public event](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubevent.gif "Public event") | [TransferredProjectStandards](8c9b377b-1416-01b2-91ec-5ceb04ae55b3.htm) | Subscribe to the TransferredProjectStandards event to be notified after the scope of a Transfer Project Standards operation has been finalized. (Inherited from [UIApplication](../Autodesk.Revit.UI/UIApplication-Class.md) ) |
| ![Public event](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubevent.gif "Public event") | [TransferringProjectStandards](a7326050-7532-df52-a54a-8acd66a2a8a3.htm) | Subscribe to the TransferringProjectStandards event to be notified before the scope of an impending Transfer Project Standards operation has been finalized in the Transfer Project Standards dialog. (Inherited from [UIApplication](../Autodesk.Revit.UI/UIApplication-Class.md) ) |
| ![Public event](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubevent.gif "Public event") | [ViewActivated](b208aae7-5cbf-21b4-b70e-af2e63ece383.htm) | Subscribe to the ViewActivated event to be notified immediately after Revit has finished activating a view of a document. (Inherited from [UIApplication](../Autodesk.Revit.UI/UIApplication-Class.md) ) |
| ![Public event](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubevent.gif "Public event") | [ViewActivating](ee4212fa-e41d-5cb5-ddc3-e31bc42db881.htm) | Subscribe to the ViewActivating event to be notified when Revit is just about to activate a view of a document. (Inherited from [UIApplication](../Autodesk.Revit.UI/UIApplication-Class.md) ) |

[Top](#PageHeader) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[ApplicationEntryPoint Class](Application-Entry-Point-Class.md) [Autodesk.Revit.UI.Macros Namespace](b95f100a-6cb5-12b3-9b2d-01bc661452db.htm)
